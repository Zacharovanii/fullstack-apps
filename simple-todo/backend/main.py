import uvicorn
from fastapi import FastAPI
from loguru import logger

from core import setup_logging

app = FastAPI()


@app.get("/")
def hello():
    return {"data": "hello world!"}


def main():
    setup_logging()
    logger.info("App start")
    logger.warning("TESTING")
    uvicorn.run("main:app")


if __name__ == "__main__":
    main()
