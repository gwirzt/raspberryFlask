from flask import Flask, render_template, request, jsonify
from db import Base, engine, session, or_

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

from models.producto  import Producto
from models.empleado import Empleado

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import redirect
from flask_babel import Babel
from flask_paginate import Pagination


app = Flask(__name__)

babel = Babel(app)

# Configuración de la base de datos
app.config['SECRET_KEY'] = 'tu_clave_secreta' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la extensión SQLAlchemy
Base.metadata.create_all(engine)

admin = Admin(app, name='Admin', template_mode='bootstrap3')
admin.add_view(ModelView(Empleado, session))
admin.add_view(ModelView(Producto, session))




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compras')
def compras():
    return render_template('compras.html')

@app.route('/ventas')
def ventas():
    return render_template('ventas.html')

@app.route('/archivos')
def archivos():
    return render_template('archivos.html')

@app.route('/productos',methods=['GET', 'POST'])
def articulos():
    pagina = request.args.get('pagina', 1, type=int)
    palabra_clave = request.args.get('palabra_clave', '', type=str)
    if palabra_clave:
        consulta = session.query(Producto).filter(or_(Producto.nombre.contains(palabra_clave), Producto.descripcion.contains(palabra_clave))).paginate(page=pagina, per_page=10)
    else:
        consulta = session.query(Producto)
        
    productos = consulta.paginate(page=pagina, per_page=10)
    
    return render_template('productos.html', productos=productos)
    

# @app.route('/archivos')
# def archivos():
#     return redirect(admin.url)

# @app.route('/archivos2')
# def archivos2():
#     return redirect(admin.url)




if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
