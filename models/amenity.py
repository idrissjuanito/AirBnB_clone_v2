#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv

from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Amenity(BaseModel, Base):
    if getenv('HBNB_STORAGE_DB') == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary='place_amenity', viewonly=False,
                                       backref='amenities')
    else:
        name = ''
