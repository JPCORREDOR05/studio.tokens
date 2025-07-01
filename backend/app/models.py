from sqlalchemy import Column, Integer, String, BigInteger, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50), default="admin")

    models = relationship("Model", back_populates="creator")

class Model(Base):
    __tablename__ = "models"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    id_number = Column(String(20), nullable=False)
    email = Column(Text)
    chaturbate_username = Column(Text, unique=True)
    stripchat_username = Column(Text, unique=True)
    schedule = Column(Text)
    created_by = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"))

    creator = relationship("User", back_populates="models")
    tokens_chaturbate = relationship("TokensChaturbate", back_populates="model")
    tokens_stripchat = relationship("TokensStripchat", back_populates="model")

class TokensChaturbate(Base):
    __tablename__ = "tokens_diarios_chaturbate"
    id = Column(BigInteger, primary_key=True, index=True)
    sub_account = Column(Text, nullable=False)
    fecha = Column(Date, nullable=False)
    tokens = Column(Integer, nullable=False)
    modelo_id = Column(BigInteger, ForeignKey("models.id", ondelete="SET NULL"))

    model = relationship("Model", back_populates="tokens_chaturbate")

class TokensStripchat(Base):
    __tablename__ = "tokens_diarios_stripchat"
    id = Column(BigInteger, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    tokens = Column(Integer, nullable=False)
    modelo_id = Column(BigInteger, ForeignKey("models.id", ondelete="SET NULL"))

    model = relationship("Model", back_populates="tokens_stripchat")
