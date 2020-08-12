#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, 
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_city import City


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nulleable = False)
    cities = relationship("City", backref="states", cascade="all, delete")
