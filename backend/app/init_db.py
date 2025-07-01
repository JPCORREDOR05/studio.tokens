import os
import secrets
import time
from sqlalchemy.exc import OperationalError
from .database import Base, engine, SessionLocal
from .models import User
from .auth import get_password_hash

USERNAME = os.getenv("SUPERADMIN_USERNAME", "juan-pablo")


def _wait_for_db(retries: int = 10, delay: int = 2):
    """Wait until the database is ready to accept connections."""
    for _ in range(retries):
        try:
            with engine.connect() as conn:
                return
        except OperationalError:
            print("Database not ready, waiting...")
            time.sleep(delay)
    raise RuntimeError("Database connection failed")


def init_db():
    _wait_for_db()
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == USERNAME).first()
        if user:
            return
        password = secrets.token_urlsafe(12)
        hashed = get_password_hash(password)
        user = User(username=USERNAME, password=hashed, role="superadmin")
        db.add(user)
        db.commit()
        print(f"Created superadmin '{USERNAME}' with password: {password}")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
