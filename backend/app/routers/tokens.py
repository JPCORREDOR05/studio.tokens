from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import auth, schemas, models, crud

router = APIRouter(prefix="/tokens", tags=["tokens"])

@router.post("/chaturbate", response_model=schemas.Tokens)
def create_tokens_chaturbate(data: schemas.TokensChaturbateCreate, current_user: models.User = Depends(auth.get_current_active_user), db: Session = Depends(auth.get_db)):
    return crud.create_tokens_chaturbate(db, data)

@router.post("/stripchat", response_model=schemas.Tokens)
def create_tokens_stripchat(data: schemas.TokensStripchatCreate, current_user: models.User = Depends(auth.get_current_active_user), db: Session = Depends(auth.get_db)):
    return crud.create_tokens_stripchat(db, data)
