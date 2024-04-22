from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ChoreDB(Base):
    __tablename__ = "chores"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    points = Column(Integer)
    status = Column(Enum("pending", "completed", name="status_enum"))
    due_date = Column(DateTime)
    assigned_to = Column(String, ForeignKey("children.name"))

class PrizeDB(Base):
    __tablename__ = "prizes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    points_required = Column(Integer)
    status = Column(Enum("available", "claimed", name="status_enum"))

class ChildDB(Base):
    __tablename__ = "children"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    total_points = Column(Integer)
    hashed_password = Column(String)
    chores = relationship("ChoreDB", backref="child")
