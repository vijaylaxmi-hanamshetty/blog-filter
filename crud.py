from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from datetime import datetime
from models import Post, Tag

def get_posts(db: Session, search: str = None, category_id: int = None, tag_id: int = None, 
              start_date: datetime = None, end_date: datetime = None, skip: int = 0, limit: int = 10):
    query = db.query(Post)

    if search:
        query = query.filter(or_(Post.title.contains(search), Post.content.contains(search)))

    if category_id:
        query = query.filter(Post.category_id == category_id)

    if tag_id:
        query = query.join(Post.tags).filter(Tag.id == tag_id)

    if start_date and end_date:
        query = query.filter(and_(Post.created_at >= start_date, Post.created_at <= end_date))

    return query.offset(skip).limit(limit).all()

def count_posts(db: Session, search: str = None, category_id: int = None, tag_id: int = None,
                start_date: datetime = None, end_date: datetime = None):
    query = db.query(Post)

    if search:
        query = query.filter(or_(Post.title.contains(search), Post.content.contains(search)))

    if category_id:
        query = query.filter(Post.category_id == category_id)

    if tag_id:
        query = query.join(Post.tags).filter(Tag.id == tag_id)

    if start_date and end_date:
        query = query.filter(and_(Post.created_at >= start_date, Post.created_at <= end_date))

    return query.count()
