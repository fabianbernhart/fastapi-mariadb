import uvicorn
from fastapi import FastAPI

from src.db import models
from src.db.database import engine
from src.router import (users_router, items_router)
from src.core.config import get_settings, Settings

settings: Settings = get_settings()


models.Base.metadata.create_all(bind=engine)

app: FastAPI = FastAPI(
    debug=settings.app_debug,
    redoc_url="/",
)


def include_routes(_app: FastAPI):
    _app.include_router(router=users_router.router, tags=["User"])
    _app.include_router(router=items_router.router, tags=["Items"])


include_routes(app)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info", env_file=".env")