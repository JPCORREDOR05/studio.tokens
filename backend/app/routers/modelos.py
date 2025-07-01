from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import auth, schemas, models, crud

router = APIRouter(prefix="/models", tags=["models"])

@router.post("/", response_model=schemas.Model)
def create_model(model: schemas.ModelCreate, current_user: models.User = Depends(auth.get_current_active_user), db: Session = Depends(auth.get_db)):
    return crud.create_model(db, model, current_user.id)

@router.get("/", response_model=list[schemas.Model])
def list_models(current_user: models.User = Depends(auth.get_current_active_user), db: Session = Depends(auth.get_db)):
    return crud.get_models(db, current_user.id)

@router.delete("/{model_id}")
def delete_model(model_id: int, current_user: models.User = Depends(auth.get_current_active_user), db: Session = Depends(auth.get_db)):
    model = crud.delete_model(db, model_id, current_user.id)
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    return {"ok": True}
