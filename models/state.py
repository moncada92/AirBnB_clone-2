#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states", cascade="all, delete")

    @property
    def cities(self):
        """get cities with id states"""
        cities = []
        allCities = storage.all(City)

        for city in allCities:
            if city.id == self.id:
                cities.append(city)
        return cities
