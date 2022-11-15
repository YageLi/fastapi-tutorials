from fastapi import APIRouter
from fastapi import Depends, status, Response, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas, db:Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id: int, request: schemas, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not found')

    blog.update(request, synchronize_session=False)
    db.commit()
    return 'updated'