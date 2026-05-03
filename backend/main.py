from fastapi import FastAPI

from app.db.database import Base, engine

from app.models import user, project, task

from app.api import auth

app = FastAPI()

print("Creating tables...")
Base.metadata.create_all(bind = engine)
print("done...")

app.include_router(auth.router, prefix = "/auth", tags = ["Auth"])

@app.get("/")
def root():
    return {"message": "API is running..."}