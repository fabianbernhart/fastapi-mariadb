from fastapi import FastAPI

from src.db import models
from src.db.database import engine
from src.router import (users_router, items_router)

models.Base.metadata.create_all(bind=engine)

app: FastAPI = FastAPI(
    debug=True,
)


def include_routes(_app: FastAPI):
    _app.include_router(router=users_router.router, tags=["User"])
    _app.include_router(router=items_router.router, tags=["Items"])


include_routes(app)
