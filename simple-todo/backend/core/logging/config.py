import sys

from ..config import get_settings

settings = get_settings()

dev_format = (
    "<green>{time:YYYY-MM-DDTHH:mm:ssZZ}</green> | "
    "<level>{level:^8}</level> | "
    "<cyan>{name:30}</cyan>:<cyan>{function:20}</cyan> | "
    "<level>{message}</level>"
)

LOGGING_CONFIG = {
    "handlers": [
        {
            "sink": sys.stdout,
            "format": dev_format,
            "level": settings.logging.level,
            "colorize": True,
        },
        {
            "sink": settings.logging.log_path,
            "format": "{message}",
            "level": "DEBUG",
            "serialize": True,
            "rotation": settings.logging.rotation,
            "retention": settings.logging.retention,
        },
    ]
}
