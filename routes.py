#  Copyright (c) 2024.
#  Julio Cezar Riffel
#  https://www.linkedin.com/in/julio-cezar-riffel/
#  https://github.com/julioriffel

from fastapi import APIRouter, Request

from core.redis import get_redis_sync
from schemas import Transaction, ClientOut
from services.service_client import ServiceClient

router = APIRouter(prefix="/clientes", tags=["clientes"])
redis = get_redis_sync()



@router.post("/{cliente_id}/transacoes")
async def post_transaction(
        request: Request,
        cliente_id: int,
        transacao: Transaction,
):
    async with request.app.state.pool.acquire() as conn:
        return await ServiceClient.save_transaction(conn, cliente_id, transacao)


@router.get("/{cliente_id}/extrato")
async def get_extrato(request: Request, cliente_id: int):
    async with request.app.state.pool.acquire() as conn:
        return await ServiceClient.statements(conn, cliente_id)
