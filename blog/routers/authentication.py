from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models, hashing
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user found')
    if not hashing.Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')

    return user