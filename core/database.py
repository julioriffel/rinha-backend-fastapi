#  Copyright (c) 2024.
#  Julio Cezar Riffel
#  https://www.linkedin.com/in/julio-cezar-riffel/
#  https://github.com/julioriffel

import asyncpg

from .config import settings


async def get_pool() -> asyncpg.pool.Pool:
    pool = await asyncpg.create_pool(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        min_size=settings.DB_MIN_SIZE,
        max_size=settings.DB_MAX_SIZE,
    )
    if not pool:
        raise Exception("Could not create pool")
    return pool
