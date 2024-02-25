from fastapi import APIRouter, HTTPException
from fastapi.params import Depends

from src.crud.users import get_user_manager, UserManager
from src.schema.users_schema import UserCreate, User

router: APIRouter = APIRouter(
    prefix="/api/v1/users",
)


@router.get("/", response_model=list[User])
def read_users(
        skip: int = 0,
        limit: int = 100,
        user_manager: UserManager = Depends(get_user_manager)
):
    users = user_manager.get_users(skip=skip, limit=limit)
    return users


@router.post("/", tags=["Administrative"], response_model=User)
def create_user(
        user: UserCreate, user_manager: UserManager = Depends(get_user_manager)
):
    db_user = user_manager.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_manager.create_user(user=user)


@router.get("/{user_id}", response_model=User)
def read_user(
        user_id: int | str,
        user_manager: UserManager = Depends(get_user_manager)
):
    db_user = user_manager.get_user(user_id=str(user_id))
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
