from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

import schemas, database, models, auth

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_db_session() -> AsyncSession: # type: ignore
    async with database.SessionLocal() as session:
        yield session

# Authentication endpoint
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db_session)):
    async with db as session:
        async with session.begin():
            user = await session.execute(select(models.ChildDB).where(models.ChildDB.name == form_data.username))
            user = user.scalars().first()
            if not user or not auth.verify_password(form_data.password, user.hashed_password):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = auth.create_access_token(
                data={"sub": user.name}, expires_delta=access_token_expires
            )
            return {"access_token": access_token, "token_type": "bearer"}

# Protected endpoint example
@app.get("/users/me", response_model=schemas.Child)
async def read_users_me(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db_session)):
    username = auth.verify_token(token, credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"))
    async with db as session:
        async with session.begin():
            user = await session.execute(select(models.ChildDB).where(models.ChildDB.name == username))
            user = user.scalars().first()
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            return schemas.Child.from_orm(user)

# CRUD endpoints for chores, prizes, and children can be added here
