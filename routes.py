from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional
from database import get_db
from schemas import PostsResponse
from crud import get_posts, count_posts

router = APIRouter()

@router.get("/posts/search", response_model=PostsResponse)
def search_posts(q: str = Query(None), page: int = 1, size: int = 10, db: Session = Depends(get_db)):
    skip = (page - 1) * size
    posts = get_posts(db, search=q, skip=skip, limit=size)
    total = count_posts(db, search=q)
    return {"total": total, "page": page, "page_size": size, "data": posts}

@router.get("/posts/filter/category/{category_id}", response_model=PostsResponse)
def filter_posts_by_category(category_id: int = Path(...), page: int = 1, size: int = 10, db: Session = Depends(get_db)):
    skip = (page - 1) * size
    posts = get_posts(db, category_id=category_id, skip=skip, limit=size)
    total = count_posts(db, category_id=category_id)
    return {"total": total, "page": page, "page_size": size, "data": posts}

@router.get("/posts/filter/tag/{tag_id}", response_model=PostsResponse)
def filter_posts_by_tag(tag_id: int = Path(...), page: int = 1, size: int = 10, db: Session = Depends(get_db)):
    skip = (page - 1) * size
    posts = get_posts(db, tag_id=tag_id, skip=skip, limit=size)
    total = count_posts(db, tag_id=tag_id)
    return {"total": total, "page": page, "page_size": size, "data": posts}

@router.get("/posts/filter/date", response_model=PostsResponse)
def filter_posts_by_date(start_date: datetime, end_date: datetime, page: int = 1, size: int = 10, db: Session = Depends(get_db)):
    skip = (page - 1) * size
    posts = get_posts(db, start_date=start_date, end_date=end_date, skip=skip, limit=size)
    total = count_posts(db, start_date=start_date, end_date=end_date)
    return {"total": total, "page": page, "page_size": size, "data": posts}

@router.get("/posts", response_model=PostsResponse)
def combined_search_filter(
    q: Optional[str] = Query(None),
    category_id: Optional[int] = Query(None),
    tag_id: Optional[int] = Query(None),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db)
):
    skip = (page - 1) * size
    posts = get_posts(db, search=q, category_id=category_id, tag_id=tag_id, start_date=start_date, end_date=end_date, skip=skip, limit=size)
    total = count_posts(db, search=q, category_id=category_id, tag_id=tag_id, start_date=start_date, end_date=end_date)
    return {"total": total, "page": page, "page_size": size, "data": posts}
