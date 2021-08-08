#!/usr/bin/python3
""" a Python file similar to model_state.py named model_city.py that contains
the class definition of a City"""

from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.coercions import StrAsPlainColumnImpl
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """A class call City that create the table in MySQL"""
    __tablename__ = 'cities'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)

    name = Column(String(128),
                  nullable=False)

    state_id = Column(Integer,
                      ForeignKey("states.id"),
                      nullable=False)

    state = relationship("State")
