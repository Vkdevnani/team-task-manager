from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str

class ProjectResponse(BaseModel):
    id: int
    name: str
    created_by: int

    class Config:
        from_attributes = True