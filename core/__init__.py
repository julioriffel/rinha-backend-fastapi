#  Copyright (c) 2024.
#  Julio Cezar Riffel
#  https://www.linkedin.com/in/julio-cezar-riffel/
#  https://github.com/julioriffel

from .redis import get_redis_sync, get_redis_async

__all__ = [
    'get_redis_async',
    'get_redis_sync'

]
