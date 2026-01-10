import uvicorn
from fastapi import FastAPI
from loguru import logger

from core import setup_logging
from db import db_helper
from db.base import Base
from api import tasks_v1_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(fs: FastAPI):
    logger.success("BACKEND STARTING UP")

    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    logger.warning("FOR DEBUG: DROPPING ALL TABLES")
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await db_helper.dispose()
    logger.info("BACKEND SHUTDOWN")


app = FastAPI(lifespan=lifespan)
setup_logging()

app.include_router(tasks_v1_router)


def main():
    uvicorn.run("main:app", access_log=True)


if __name__ == "__main__":
    main()
