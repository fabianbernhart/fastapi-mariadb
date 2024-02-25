from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.db import models
from src.db.database import get_db
from src.schema.items_schema import ItemCreate


class ItemManager:
    def __init__(self, db: Session):
        self.db = db

    def get_items(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.Item).offset(skip).limit(limit).all()

    def create_user_item(self, item: ItemCreate, user_id: int):
        db_item = models.Item(**item.dict(), owner_id=user_id)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item


def get_item_manager(_db: Session = Depends(get_db)) -> ItemManager:
    return ItemManager(db=_db)
