import db
from sqlalchemy import Column, Integer, String, Float

class Producto(db.Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    precio = Column(Float)
    descripcion = Column(String)

    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def __str__(self):
        return f'{self.id} {self.nombre} {self.precio} {self.descripcion}'

    def __repr__(self):
        return f'{self.id} {self.nombre} {self.precio} {self.descripcion}'
    
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'descripcion': self.descripcion
        }
