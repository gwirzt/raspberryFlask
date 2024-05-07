# import db
# from sqlalchemy import Column, Integer, String, Float, DateTime

# class Cliente(db.Base):
#     __tablename__ = 'clientes'
#     id = Column(Integer, primary_key=True)
#     nombre = Column(String)
#     apellido = Column(String)
#     dni = Column(String)
#     direccion = Column(String)
#     telefono = Column(String)
#     email = Column(String)
#     tipoIva = Column(int)
#     cuit = Column(int)

    
    
#     def __init__(self, nombre, apellido, dni, direccion, telefono, email, tipoIva, cuit):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.dni = dni
#         self.direccion = direccion
#         self.telefono = telefono
#         self.email = email
#         self.tipoIva = tipoIva
#         self.cuil = cuit
        
        

#     def __str__(self):
#         return f'{self.id} {self.nombre} {self.apellido} {self.dni} {self.direccion} {self.telefono} {self.email} 
#         {self.tipoIva} {self.cuit} '

#     def __repr__(self):
#         return f'{self.id} {self.nombre} {self.apellido} {self.dni} {self.direccion} {self.telefono} {self.email}
#         {self.tipoIva} {self.cuit}'
    
#     def serialize(self):
#         return {
#             'id': self.id,
#             'nombre': self.nombre,
#             'apellido': self.apellido,
#             'dni': self.dni,
#             'direccion': self.direccion,
#             'telefono': self.telefono,
#             'email': self.email,
#             'tipoIva': self.tipoIva,
#             'cuit': self.cuit
            
#         }
