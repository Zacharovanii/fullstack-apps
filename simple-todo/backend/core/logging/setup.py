import logging

from loguru import logger

from .config import LOGGING_CONFIG


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 1
        while frame:
            # Проверяем, не является ли текущий файл частью модуля logging
            # или самим этим файлом обработчика
            filename = frame.f_code.co_filename
            if filename == logging.__file__ or filename == __file__:
                frame = frame.f_back
                depth += 1
            else:
                break

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def setup_logging():
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(logging.INFO)

    for name in logging.root.manager.loggerDict.keys():
        if name.startswith("uvicorn"):
            logging.getLogger(name).handlers = []
            logging.getLogger(name).propagate = True

    logger.remove()
    logger.configure(**LOGGING_CONFIG)
    logger.info("Standard logging redirected to Loguru")
