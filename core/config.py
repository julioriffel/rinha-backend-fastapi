#  Copyright (c) 2024.
#  Julio Cezar Riffel
#  https://www.linkedin.com/in/julio-cezar-riffel/
#  https://github.com/julioriffel

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DB_DRIVER: str = "postgresql+asyncpg"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_HOST: str = "db"
    DB_PORT: int = 5432
    DB_NAME: str = "postgres"
    DB_URL: str = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    DB_MIN_SIZE: int = 10
    DB_MAX_SIZE: int = 30

    TESTING: bool = False

    REDIS_HOST: str = "redis"


settings = Config()
