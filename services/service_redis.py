#  Copyright (c) 2024.
#  Julio Cezar Riffel
#  https://www.linkedin.com/in/julio-cezar-riffel/
#  https://github.com/julioriffel

from core import get_redis_sync, get_redis_async
from core.exceptions import LimitExceededException

from schemas import TransactionTypeEnum

redis_async = get_redis_async()
redis_sync = get_redis_sync()


class ServiceClientRedis:
    @classmethod
    def redis_limit_key(cls, id_client):
        return f'client_limit_{id_client}'

    @classmethod
    def redis_balance_key(cls, id_client):
        return f'client_balance_{id_client}'

    @classmethod
    def redis_client_lock_key(cls, id_client):
        return f'client_lock_{id_client}'

    @classmethod
    async def get_client_limit(cls, id_client):
        value = await redis_async.get(cls.redis_limit_key(id_client))
        return int(value)

    @classmethod
    async def set_client_limit_redis(cls, id_client, limit):
        await redis_async.set(cls.redis_limit_key(id_client), limit)

    @classmethod
    def get_client_balance(cls, id_client) -> int:
        try:
            value = redis_sync.get(cls.redis_balance_key(id_client))
            return int(value)
        except TypeError:
            return 0

    @classmethod
    async def set_client_balance(cls, id_client, limit):
        await redis_async.set(cls.redis_balance_key(id_client), limit)

    @classmethod
    async def persist_transaction(cls, id_client: int, amount: int, transaction_type: str, limit: int):

        if transaction_type == TransactionTypeEnum.DEBIT:
            amount = amount * -1
            balance = cls.get_client_balance(id_client)
            if balance + amount + limit < 0:
                raise LimitExceededException()
        new_balance = redis_sync.incrby(cls.redis_balance_key(id_client), amount)

        return new_balance
