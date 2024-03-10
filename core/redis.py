#  Copyright (c) 2024.
#  Julio Cezar Riffel
#  https://www.linkedin.com/in/julio-cezar-riffel/
#  https://github.com/julioriffel

import redis as redis
import redis.asyncio as redis_async

from .config import settings


def get_redis_sync():
    return redis.Redis(host=settings.REDIS_HOST, decode_responses=True)


def get_redis_async():
    return redis_async.Redis(host=settings.REDIS_HOST, decode_responses=True)
