from uuid import UUID, uuid4
from typing import List
from fastapi import FastAPI, HTTPException

from models import Gender, Role, UpdateUser, User

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("9c870293-506b-41be-b862-12a97171fd65"),
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student],
        middle_name="A.",
    ),
    User(
        id=UUID("09247c72-79d2-432c-9cff-6ebadf0dc12f"),
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin],
        middle_name="B.",
    ),
]


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/users/{user_id}")
async def fetch_user(user_id: UUID):
    user = next((user for user in db if user.id == user_id), None)
    return user


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    user = next((user for user in db if user.id == user_id), None)
    if user:
        db.remove(user)
        return {"message": f"{user.id} User deleted successfully"}
    raise HTTPException(
        status_code=404, detail=f"User with id:{user_id} does not exist"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(update_user: UpdateUser, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if update_user.first_name is not None:
                user.first_name = update_user.first_name
            if update_user.last_name is not None:
                user.last_name = update_user.last_name
            if update_user.middle_name is not None:
                user.middle_name = update_user.middle_name
            if update_user.roles is not None:
                user.roles = update_user.roles
            if update_user.gender is not None:
                user.gender = update_user.gender

            return {"message": f"{user.id} User updated successfully"}
    raise HTTPException(
        status_code=404, detail=f"User with id:{user_id} does not exist"
    )
