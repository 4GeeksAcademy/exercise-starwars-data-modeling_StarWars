import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250))
    description = Column(String(250))
    diameter = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    name = Column(String(250))
    url = Column(String(250))


class Vehicles(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250))
    description = Column(String(250))
    model = Column(String(250))
    vehicles_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_creadits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_atomsphering_speed = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    films = Column(String(250))
    pilots = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    name = Column(String(250))
    url = Column(String(250))

class Characters(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    color_eyes = Column(String(250))
    birth_year = Column(String(250))
    films = Column(String(250))
    gender = Column(String(6))
    hair_color = Column(String(250))
    height = Column(Float)
    homeworld = Column(String(250), ForeignKey(Planets.id))
    mass = Column(String(250))
    skin_color = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    spices = Column(String(250))
    starships = Column(String(250))
    url = Column(String(250))
    planets = relationship("Planets", back_populates="characters")
    vehicles = relationship("Vehicles", back_populates="characters")

class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    vehicles_id = Column(Integer, ForeignKey(Vehicles.id))
    planets_id = Column(Integer, ForeignKey(Planets.id))
    characters_id = Column(Integer, ForeignKey(Characters.id))
    favorites = Column(Enum('personaje', 'vehiculo', 'planeta', name='favorite_type'))
    usuario = relationship("Usuario", back_populates="favorites")
    characters = relationship("Characters", back_populates="favorites")
    planets = relationship("Planets", back_populates="favorites")
    vehicles = relationship("Vehicles", back_populates="favorites")

class Usuario(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    apellido = Column(String(250))
    email = Column(String(250))
    direccion = Column(String(250))
    telefono = Column(String(250))
    celular = Column(String(250))
    fecha_ingreso = Column(String(250))
    usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    login = relationship("Login", back_populates="usuario")
    favorites = relationship("Favorites", back_populates="usuario")

class Login(Base):
    __tablename__ = 'Login'
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    password = Column(String(250))
    usuario_id = Column(String(250), ForeignKey(Usuario.id))
    usuario = relationship("Usuario", back_populates="login")
    
class FavoritePlanets(Base):
    __tablename__ = 'FavoritePlanets'
    id = Column(Integer, primary_key=True)
    favorites_id = Column(Integer, ForeignKey('Favorites.id'))
    planets_id = Column(Integer, ForeignKey('Planets.id'))
    favorites = relationship("Favorites", back_populates="favorite_planets")
    planet = relationship("Planets", back_populates="favorite_planets")
    Favorites.favorite_planets = relationship("FavoritePlanets", back_populates="favorites")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
