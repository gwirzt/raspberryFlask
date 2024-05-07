# from flask import request, jsonify
# from db import session
# from models.cliente import Cliente
# import json

# def create_cliente():
    
#     data = request.json

#     nombre = data.get('nombre')
#     apellido = data.get('apellido')
#     dni = data.get('dni')
#     direccion = data.get('direccion')
#     telefono = data.get('telefono')
#     email = data.get('email')
#     tipoIva = data.get('tipoIva')
#     cuit = data.get('cuit')

#     nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, dni=dni, direccion=direccion, telefono=telefono, email=email, tipoIva=tipoIva, cuit=cuit)

#     session.add(nuevo_cliente)
    
#     session.commit()

#     return jsonify({'message': 'Cliente creado exitosamente'}), 201
