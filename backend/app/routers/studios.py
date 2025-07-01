from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import auth, schemas, models, crud

router = APIRouter(prefix="/studios", tags=["studios"])

@router.get("/me", response_model=schemas.User)
def read_users_me(current_user: models.User = Depends(auth.get_current_active_user)):
    return current_user


@router.get("/", response_model=list[schemas.User])
def list_studios(current_user: models.User = Depends(auth.get_current_active_user), db: Session = Depends(auth.get_db)):
    if current_user.role != "superadmin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return crud.get_users(db)


@router.post("/", response_model=schemas.User)
def create_studio(user: schemas.UserCreate, current_user: models.User = Depends(auth.get_current_active_user), db: Session = Depends(auth.get_db)):
    if current_user.role != "superadmin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db, user)


@router.delete("/{user_id}")
def delete_studio(user_id: int, current_user: models.User = Depends(auth.get_current_active_user), db: Session = Depends(auth.get_db)):
    if current_user.role != "superadmin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    success = crud.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"ok": True}
