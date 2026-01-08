from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from core import get_settings


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=get_settings().db.naming_convention)
