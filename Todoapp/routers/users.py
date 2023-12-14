from typing import Annotated

from passlib.context import CryptContext
from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from starlette import status
from models import  Users
from database import SessionLocal
from .auth import get_current_user

router = APIRouter(
    prefix="/user",
    tags=['user']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Adding injection dependency for our database connection
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)

@router.get(path="/", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    user = db.query(Users).filter(Users.id == user.get('id')).first()
    return user

@router.put(path="/password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')

    user = db.query(Users).filter(Users.id == user.get('id')).first()

    if not bcrypt_context.verify(user_verification.password, user.hashed_password):
        raise HTTPException(status_code=401, detail='Error on password change')

    user.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user)
    db.commit()

@router.get(path="/{user_id}", status_code=status.HTTP_200_OK)
async def get_users(db: db_dependency, user_id: int = Path(gt=0)):
    user = db.query(Users).filter(Users.id == user_id).first()

    if user is not None:
        return user
    else:
        raise HTTPException(status_code=404, detail='User not found.')
