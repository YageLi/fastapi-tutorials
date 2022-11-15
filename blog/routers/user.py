from fastapi import APIRouter
from fastapi import FastAPI, Depends, status, Response, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash
from typing import List
from ..database import get_db

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post('/', response_model=schemas.Show_User)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashedPwd = Hash.bcrypt(request.password)
    new_user = models.User(name=request.name,email=request.email, password=hashedPwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}', response_model=schemas.Show_User)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available')
    return user