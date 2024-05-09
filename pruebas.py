from flask import Flask, render_template, request
import requests
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)

# Función para obtener los datos de la API de JSONPlaceholder
def get_posts(page=1, limit=10):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts?_page={page}&_limit={limit}")
    if response.status_code == 200:
        return response.json(), response.headers.get('X-Total-Count', 0)
    else:
        return [], 0

# Ruta para obtener la lista de publicaciones paginada
@app.route('/', methods=['GET'])
def obtener_publicaciones():
    # Parámetros de paginación
    pagina = request.args.get(get_page_parameter(), type=int, default=1)
    limite = 10

    # Obtener los datos de la API
    posts, total_posts = get_posts(page=pagina, limit=limite)

    # Configurar la paginación
    pagination = Pagination(page=pagina, total=total_posts, per_page=limite, css_framework='bootstrap4')

    return render_template('pruebas.html', posts=posts, pagination=pagination)

if __name__ == '__main__':
    app.run(debug=True)


