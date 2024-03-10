#  Copyright (c) 2024.
#  Julio Cezar Riffel
#  https://www.linkedin.com/in/julio-cezar-riffel/
#  https://github.com/julioriffel

from datetime import datetime

from async_lru import alru_cache

from schemas import Client, Transaction
from services.database import ServiceDatabase
from services.service_redis import ServiceClientRedis


class ServiceClient:

    @classmethod
    @alru_cache(maxsize=512, ttl=600)
    async def get_client(cls, id_client: int, conn) -> Client:
        try:
            limite = await ServiceClientRedis.get_client_limit(id_client)
        except TypeError:
            limite = await ServiceDatabase.get_client_limit(conn, id_client)
            await ServiceClientRedis.set_client_balance(id_client, 0)
            await ServiceClientRedis.set_client_limit_redis(id_client, limite)
        return Client(id=id_client, limite=limite)

    @classmethod
    async def save_transaction(cls, conn, id_client: int, transaction: Transaction):
        client = await cls.get_client(id_client, conn)
        await ServiceClientRedis.persist_transaction(id_client, transaction.valor, transaction.tipo, client.limite)
        await ServiceDatabase.transaction_insert(conn, id_client, transaction)
        return client

    @classmethod
    async def statements(cls, conn, cliente_id):

        client = await cls.get_client(cliente_id, conn)
        last_transactions = await ServiceDatabase.last_transactions(conn, cliente_id)

        extrato = {
            "saldo": {
                "total": client.saldo,
                "limite": client.limite,
                "data": datetime.now()
            },
            "ultimas_transacoes": [
                {
                    "valor": row["valor"],
                    "tipo": row["tipo"],
                    "descricao": row["descricao"],
                    "realizada_em": row["realizada_em"],
                }
                for row in last_transactions
            ],

        }
        return extrato
