from flask import request, jsonify
from db import session
from models import Producto

def create_product():
    # Obtener el JSON enviado en la solicitud
    data = request.json

    # Extraer los datos del JSON
    nombre = data.get('nombre')
    precio = data.get('precio')
    descripcion = data.get('descripcion')

    # Crear una nueva instancia de Producto con los datos extraídos
    nuevo_producto = Producto(nombre=nombre, precio=precio, descripcion=descripcion)

    # Agregar el nuevo producto a la sesión
    session.add(nuevo_producto)
    
    # Commit para guardar el nuevo producto en la base de datos
    session.commit()

    return jsonify({'message': 'Producto creado exitosamente'}), 201

def read_products():
    productos = productos = session.query(Producto).all() 
    return jsonify([producto.serialize() for producto in productos])    


