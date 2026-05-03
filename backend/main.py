from fastapi import FastAPI

from app.db.database import Base, engine

from app.models import user, project, task

app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.get("/")
def root():
    return {"message": "API is running, database connected and tables created"}