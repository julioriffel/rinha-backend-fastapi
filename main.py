#  Copyright (c) 2024.
#  Julio Cezar Riffel
#  https://www.linkedin.com/in/julio-cezar-riffel/
#  https://github.com/julioriffel

from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.database import get_pool
from routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        app.state.pool = await get_pool()
        yield
    finally:
        await app.state.pool.close()


app = FastAPI(lifespan=lifespan, docs_url=None, redoc_url=None)
app.include_router(router)
