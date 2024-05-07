from flask import Flask, render_template, request, jsonify
from db import Base, engine, session

from models.producto  import Producto
from models.empleado import Empleado
#from controllers.producto import create_product, articulos_show
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import redirect
from flask_babel import Babel



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
    return redirect(admin.url)

@app.route('/archivos2')
def archivos2():
    return redirect(admin.url)




if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
