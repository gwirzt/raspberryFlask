from flask import Flask, render_template, request, jsonify
from db import Base, engine
from models import Producto
from controllers import create_product, read_products




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

@app.route('/productos', methods=['POST'])
def create():
    return create_product()

@app.route('/productos', methods=['GET'])
def read():
    return read_products()


    
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
