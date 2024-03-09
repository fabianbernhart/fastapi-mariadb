from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "fastapi-mariadb-sqlalchemy"
    app_debug: bool = False
    sqlalchemy_database_url: str = ""

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()


print(get_settings())