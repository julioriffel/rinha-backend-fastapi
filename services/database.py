#  Copyright (c) 2024.
#  Julio Cezar Riffel
#  https://www.linkedin.com/in/julio-cezar-riffel/
#  https://github.com/julioriffel

from async_lru import alru_cache

from core.exceptions import NotFoundException
from schemas import Transaction


class ServiceDatabase:

    @classmethod
    @alru_cache(ttl=600)
    async def get_client_limit(cls, conn, cliente_id: int) -> int:
        stmt = "SELECT limite FROM cliente WHERE id = $1"
        limit = await conn.fetchval(stmt, cliente_id)
        if not limit:
            raise NotFoundException()
        return limit

    @classmethod
    async def transaction_insert(cls, conn, cliente_id: int, transaction: Transaction):
        stmt = "INSERT INTO transacao(cliente_id,tipo, valor, descricao,realizada_em) VALUES ($1, $2, $3, $4, now())"
        await conn.execute(
            stmt,
            cliente_id,
            transaction.tipo,
            transaction.valor,
            transaction.descricao,
        )

    @classmethod
    async def last_transactions(cls, conn, cliente_id):
        stmt = ("SELECT tipo, valor, descricao, realizada_em"
                " FROM transacao"
                " WHERE cliente_id = $1"
                " ORDER BY id"
                " DESC LIMIT 10")

        return await conn.fetch(stmt, cliente_id)
