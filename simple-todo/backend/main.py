import uvicorn
from fastapi import FastAPI
from loguru import logger

from core import setup_logging

app = FastAPI()
setup_logging()


def main():
    logger.success("BACKEND STARTING UP")
    logger.warning("TEST")
    uvicorn.run("main:app", access_log=True)


if __name__ == "__main__":
    main()
