from fastapi import APIRouter

user_router = APIRouter(prefix="/user")

@user_router.get("/")
async def get_users():
    return {"Hello": "World"} 