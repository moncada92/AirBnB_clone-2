#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.amenity import Amenity
from os import getenv
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            from models import storage

            our_rv = storage.all(Review)
            revs = []
            for value in our_rv.values():
                if self.id == place.id:
                    revs.append(value)
            return revs

        @property
        def amenities(self):
            our_am = storage.all(Amenity)
            amen = []
            for value in our_am.values():
                if amenities_ids == amenity.ids:
                    amen.append(value)
            return amen

        @amenities.setter
        def amenities(self, obj):
            if type(obj) == 'Amenity':
                self.amenity_ids.append(obj.id)
