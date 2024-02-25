from fastapi import APIRouter
from fastapi.params import Depends

from src.crud.items import get_item_manager, ItemManager
from src.schema.items_schema import Item, ItemCreate

router: APIRouter = APIRouter(
    prefix="/api/v1/items",
)


@router.post("/", response_model=Item)
def create_item_for_user(
    user_id: int,
    item: ItemCreate,
    item_manager: ItemManager = Depends(get_item_manager),
):
    return item_manager.create_user_item(item=item, user_id=user_id)


@router.get("/", response_model=list[Item])
def read_items(
    skip: int = 0,
    limit: int = 100,
    item_manager: ItemManager = Depends(get_item_manager),
):
    items = item_manager.get_items(skip=skip, limit=limit)
    return items

