from datetime import datetime
from app.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, nullable = False)
    description = Column(String)
    status = Column(String, default = "TODO")
    due_date = Column(DateTime)
    assigned_to = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))