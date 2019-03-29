#!/usr/bin/python3
"""
class definition for state
"""


from sqlalchemy import Column, Integer, String
import MySQLdb


Base = declarative_base()


class State(Base):
    """
    inherits from Base, states table object
    """

    __table_name__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
