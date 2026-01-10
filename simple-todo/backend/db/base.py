from typing import Annotated

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, mapped_column

from core import get_settings


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=get_settings().db.naming_convention)


primary_key = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
unique_str = Annotated[str, mapped_column(unique=True)]
