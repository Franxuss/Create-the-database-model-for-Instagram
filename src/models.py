import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    email = Column(String)
    password = Column(String)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('user.id'))
#     person = relationship(User)

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    user = Column(String)
    date = Column(String)
  

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    image = Column(String)
    date = Column(String)
    user = Column(String)

class DirectMessage(Base):
    __tablename__ = 'directMessage'
    id = Column(Integer, primary_key=True)
    user = Column(String)
    date = Column(String)
    voicenote = Column(String)
    message = Column(String(300))
    image = Column(String)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')