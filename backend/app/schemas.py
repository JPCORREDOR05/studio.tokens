from datetime import date
from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    role: str = "admin"

class User(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True

class ModelBase(BaseModel):
    name: str
    id_number: str
    email: Optional[str] = None
    chaturbate_username: Optional[str] = None
    stripchat_username: Optional[str] = None
    schedule: Optional[str] = None

class ModelCreate(ModelBase):
    pass

class Model(ModelBase):
    id: int
    created_by: int

    class Config:
        orm_mode = True

class TokensBase(BaseModel):
    fecha: date
    tokens: int

class TokensChaturbateCreate(TokensBase):
    sub_account: str
    modelo_id: Optional[int] = None

class TokensStripchatCreate(TokensBase):
    modelo_id: Optional[int] = None

class Tokens(TokensBase):
    id: int
    modelo_id: Optional[int]

    class Config:
        orm_mode = True
