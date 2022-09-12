#!/usr/bin/python3
"""
State class:
	inherits from Base Tips
	links to the MySQL table states
	attributes:
		id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
		name that represents a column of a string with maximum 128 characters and can’t be null
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ defining class """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
