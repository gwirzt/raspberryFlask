from flask import Flask, render_template, request, jsonify

users = {
    'gwirzt': {'password':'clave1','token': '1211Gustavo'},
    'psormani': {'password':'clave1','token':  '1305Patricia'}
}


app = Flask(__name__)

@app.route('/')
def index():
    return 'Página principal'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        token = request.form['token']

        if username in users and users[username]['password'] == password and users[username]['token'] == token:
            return jsonify({'message': 'Inicio de sesión exitoso'})
        else:
            return jsonify({'message': 'Credenciales inválidas'}), 401
    else:
        return render_template('login.html')


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
