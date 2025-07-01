from sqlalchemy.orm import Session
from . import models, schemas, auth
from typing import List

# User operations
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session) -> List[models.User]:
    return db.query(models.User).all()


def delete_user(db: Session, user_id: int) -> bool:
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

# Model operations
def create_model(db: Session, model: schemas.ModelCreate, user_id: int):
    db_model = models.Model(**model.dict(), created_by=user_id)
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model


def get_models(db: Session, user_id: int):
    return db.query(models.Model).filter(models.Model.created_by == user_id).all()


def get_model(db: Session, model_id: int, user_id: int):
    return db.query(models.Model).filter(models.Model.id == model_id, models.Model.created_by == user_id).first()


def delete_model(db: Session, model_id: int, user_id: int):
    model = get_model(db, model_id, user_id)
    if model:
        db.delete(model)
        db.commit()
    return model

# Token operations
def create_tokens_chaturbate(db: Session, token_data: schemas.TokensChaturbateCreate):
    db_token = models.TokensChaturbate(**token_data.dict())
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token


def create_tokens_stripchat(db: Session, token_data: schemas.TokensStripchatCreate):
    db_token = models.TokensStripchat(**token_data.dict())
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

# Reporting helpers
def tokens_summary(db: Session, user_id: int, trm: float):
    """Return total tokens and amounts per model for a user."""
    results = []
    models_q = db.query(models.Model).filter(models.Model.created_by == user_id).all()
    for m in models_q:
        chaturbate_total = sum(t.tokens for t in m.tokens_chaturbate)
        stripchat_total = sum(t.tokens for t in m.tokens_stripchat)
        tokens = chaturbate_total + stripchat_total
        usd = tokens * 0.05
        cop = usd * trm
        results.append({
            "model_id": m.id,
            "name": m.name,
            "tokens": tokens,
            "usd": usd,
            "cop": cop,
        })
    total_usd = sum(r["usd"] for r in results)
    total_cop = sum(r["cop"] for r in results)
    return {"models": results, "total_usd": total_usd, "total_cop": total_cop}
