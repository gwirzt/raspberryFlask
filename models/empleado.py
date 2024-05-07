import db
from sqlalchemy import Column, Integer, String, Float, DateTime


class Empleado(db.Base):
    __tablename__ = 'empleados'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    dni = Column(String)
    direccion = Column(String)
    telefono = Column(String)
    email = Column(String)
    fechaNacimiento = Column(DateTime)  
    fechaIngreso = Column(DateTime)
    
    
    def __init__(self, nombre, apellido, dni, direccion, telefono, email, fechaNacimiento, fechaIngreso):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fechaNacimiento = fechaNacimiento
        self.fechaIngreso = fechaIngreso
        
        

    def __str__(self):
        return f'{self.id} {self.nombre} {self.apellido} {self.dni} {self.direccion} {self.telefono} {self.email} {self.fechaNacimiento} {self.fechaIngreso}'

    def __repr__(self):
        return f'{self.id} {self.nombre} {self.apellido} {self.dni} {self.direccion} {self.telefono} {self.email} {self.fechaNacimiento} {self.fechaIngreso}'
    
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'dni': self.dni,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'email': self.email,
            'fechaNacimiento': self.fechaNacimiento,
            'fechaIngreso': self.fechaIngreso
            
        }
