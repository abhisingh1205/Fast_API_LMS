from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing student and courses. ",
    
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": "Hello World"}

@app.get("/users/{id}")
async def get_user(id: int = Path(..., description="The ID of the USer we want", gt=2), q: str = Query(None, max_length=5)):
    return {"user": users[id], "query": q}