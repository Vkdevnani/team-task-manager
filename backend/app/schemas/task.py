from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    due_date: datetime | None = None
    assigned_to: int
    project_id: int

class TaskUpdate(BaseModel):
    status: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    due_date: datetime | None
    assigned_to: int
    project_id: int

    class Config:
        from_attributes = True