import uvicorn
from fastapi import FastAPI

from api import tasks_v1_router
from core import setup_logging
from lifespan import lifespan


def run():
    setup_logging()

    app = FastAPI(lifespan=lifespan)
    app.include_router(tasks_v1_router)

    return app


if __name__ == "__main__":
    uvicorn.run("main:run", access_log=True, factory=True)
