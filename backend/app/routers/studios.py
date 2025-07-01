from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import auth, schemas, models, crud

router = APIRouter(prefix="/studios", tags=["studios"])

@router.get("/me", response_model=schemas.User)
def read_users_me(current_user: models.User = Depends(auth.get_current_active_user)):
    return current_user
