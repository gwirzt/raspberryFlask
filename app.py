from flask import Flask, render_template, request, jsonify
from db import Base, engine
from models.producto  import Producto
from controllers.producto import create_product, articulos_show




app = Flask(__name__)


# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la extensión SQLAlchemy
Base.metadata.create_all(engine)

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

# @app.route('/articulos', methods=['POST'])
# def create():
#     return create_product()

@app.route('/articulos_show', methods=['GET'])
def articulos_listar():
    productos_json = articulos_show()  # Llama a la función que devuelve los datos de los productos
    print(productos_json)
    return render_template('articulos_show.html', productos=productos_json)  # Pasa los datos a la plantilla

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
