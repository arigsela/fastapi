from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Chore(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    points: int
    status: str  # e.g., "pending", "completed"
    due_date: datetime
    assigned_to: str  # child's name or identifier

class Prize(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    points_required: int
    status: str  # e.g., "available", "claimed"

class Child(BaseModel):
    id: Optional[int] = None
    name: str
    total_points: int
    password: str

class ChildPointsUpdate(BaseModel):
    points_earned: int
