from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import auth, models, crud, schemas
import os

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/summary", response_model=schemas.Summary)
def summary(current_user: models.User = Depends(auth.get_current_active_user), db: Session = Depends(auth.get_db)):
    trm = float(os.getenv("TRM_RATE", "4000"))
    return crud.tokens_summary(db, current_user.id, trm)
