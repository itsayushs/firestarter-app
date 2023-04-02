from fastapi import APIRouter

router = APIRouter()

@router.get("/posts")
def get_posts():
    return [
        {"title": "Hello, world!", "data": "this is my first post"},
        {"title": "New Day", "data": "this is my second post.. about a new day"}
    ]