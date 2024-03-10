#  Copyright (c) 2024.
#  Julio Cezar Riffel
#  https://www.linkedin.com/in/julio-cezar-riffel/
#  https://github.com/julioriffel

from enum import Enum

from pydantic import BaseModel, Field, PositiveInt, computed_field


class Client(BaseModel):
    id: PositiveInt
    limite: PositiveInt

    @computed_field
    def saldo(self) -> int:
        from services.service_redis import ServiceClientRedis
        return ServiceClientRedis.get_client_balance(self.id)


class ClientOut(BaseModel):
    limite: int
    saldo: int


class TransactionTypeEnum(str, Enum):
    CREDIT = "c"
    DEBIT = "d"


class Transaction(BaseModel):
    valor: PositiveInt
    tipo: TransactionTypeEnum
    descricao: str = Field(..., min_length=1, max_length=10)
