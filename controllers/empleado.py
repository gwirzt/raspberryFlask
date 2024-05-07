# from flask import request, jsonify
# from db import session
# from models.empleado import Empleado
# import json

# def create_empleado():
#     # Obtener el JSON enviado en la solicitud
#     data = request.json

#     # Extraer los datos del JSON
#     nombre = data.get('nombre')
#     apellido = data.get('apellido')
#     dni = data.get('dni')
#     direccion = data.get('direccion')
#     telefono = data.get('telefono')
#     email = data.get('email')
#     fechaNacimiento = data.get('fechaNacimiento')
#     fechaIngreso = data.get('fechaIngreso')

#     # Crear una nueva instancia de Producto con los datos extraídos
#     nuevo_empleado = Empleado(nombre=nombre, apellido=apellido, dni=dni, direccion=direccion, telefono=telefono, email=email, fechaNacimiento=fechaNacimiento, fechaIngreso=fechaIngreso)

#     # Agregar el nuevo producto a la sesión
#     session.add(nuevo_empleado)
    
#     # Commit para guardar el nuevo producto en la base de datos
#     session.commit()

#     return jsonify({'message': 'Empleado creado exitosamente'}), 201
