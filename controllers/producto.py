from flask import request, jsonify
from db import session
from models.producto import Producto
import json

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

def articulos_show():
    productos = productos = session.query(Producto).order_by(Producto.nombre).all()
    productos_json = [producto.serialize() for producto in productos]
    return json.dumps(productos_json)   


