from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_debug: False
    sqlalchemy_database_url: str = "mariadb+pymysql://root:toor@127.0.0.1:3306/company"

    model_config = SettingsConfigDict(env_prefix='my_prefix_')


def get_settings():
    return Settings()
