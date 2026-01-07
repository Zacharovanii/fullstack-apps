from loguru import logger

from .config import LOGGING_CONFIG


def setup_logging():
    logger.remove()
    logger.configure(**LOGGING_CONFIG)
