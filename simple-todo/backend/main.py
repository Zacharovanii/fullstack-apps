import uvicorn
from fastapi import FastAPI
from loguru import logger

from core import setup_logging
from db import db_helper
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(fs: FastAPI):
    logger.success("BACKEND STARTING UP")
    yield
    await db_helper.dispose()
    logger.info("BACKEND SHUTDOWN")


app = FastAPI(lifespan=lifespan)
setup_logging()


if __name__ == "__main__":
    uvicorn.run("main:app", access_log=True)
