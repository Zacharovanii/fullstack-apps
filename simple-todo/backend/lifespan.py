from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

from db import db_helper
from db.base import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.success("BACKEND STARTING UP")

    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    logger.warning("FOR DEBUG: DROPPING ALL TABLES")
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await db_helper.dispose()
    logger.info("BACKEND SHUTDOWN")
