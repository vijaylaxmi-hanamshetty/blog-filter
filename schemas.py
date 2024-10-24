from pydantic import BaseModel
from typing import List

class TagBase(BaseModel):
    name: str

class CategoryBase(BaseModel):
    name: str

class PostBase(BaseModel):
    title: str
    content: str
    category_id: int

class PostCreate(PostBase):
    tags: List[str] = []

class PostResponse(PostBase):
    id: int
    created_at: str
    tags: List[TagBase] = []

    class Config:
        from_attributes = True

class PostsResponse(BaseModel):
    total: int
    page: int
    page_size: int
    data: List[PostResponse]
