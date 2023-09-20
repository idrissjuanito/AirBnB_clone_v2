#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String


class Review(BaseModel, Base):
    """ Review class to store user reviews"""
    __tablename__ = 'reviews'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    # def __init__(self, *args, **kwargs):
    #     """initializes Place"""
    #     super().__init__(*args, **kwargs)
