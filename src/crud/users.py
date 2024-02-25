from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.db import models
from src.db.database import get_db


class UserManager:
    def __init__(self, db: Session):
        self.db = db

    def get_users(self, skip: int = 0, limit: int = 100) -> list:
        return self.db.query(models.User).offset(skip).limit(limit).all()

    def get_user_by_email(self, email: str):
        return self.db.query(models.User).filter(models.User.email == email).first()

    def create_user(self, user):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user: models.User = models.User(email=user.email, hashed_password=fake_hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, user_id: str):
        return self.db.query(models.User).filter(models.User.id == user_id).first()


def get_user_manager(_db: Session = Depends(get_db)) -> UserManager:
    return UserManager(db=_db)
