from flask import Flask, request, jsonify, send_file
from psycopg2 import connect, extras
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Credenciales para PostgreSQL
host = 'localhost'
port = 5432
dbname = 'postgres'
user = 'postgres'
password = '1234'
options = "-c client_encoding=UTF8"


def get_connection():
    conn = connect(host=host, port=port, dbname=dbname,
                   user=user, password=password)
    return conn


@app.get('/api/users')
def get_users():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    return jsonify(users)


@app.post('/api/users')
def create_user():
    new_user = request.get_json()
    username = new_user['username']
    email = new_user['email']
    password = Fernet(key).encrypt(bytes(new_user['password'], 'utf-8'))

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO public.users (username, email, password) VALUES (%s, %s, %s) RETURNING *',
                (username, email, password))
    new_created_user = cur.fetchone()
    print(new_created_user)
    conn.commit()

    cur.close()
    conn.close()

    return jsonify(new_created_user)


@ app.delete('/api/users/<id>')
def delete_user(id):
    conn = get_connection()
    # obtiene el usuario que se ha eliminado
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('DELETE FROM users WHERE id = %s RETURNING *', (id, ))
    user = cur.fetchone()

    conn.commit()
    cur.close()
    conn.close()

    # Verifica si se encontró y eliminó el usuario
    if user:
        return jsonify({'message': 'Usuario eliminado exitosamente', 'user': user}), 200
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404


@ app.put('/api/users/<id>')
def update_user(id):

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    new_user = request.get_json()
    username = new_user['username']
    email = new_user['email']
    password = Fernet(key).encrypt(bytes(new_user['password'], 'utf-8'))

    cur.execute('UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s RETURNING *',
                (username, email, password, id))
    updated_user = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    if updated_user is None:
        return ({'message': 'Usuario no encontrado'}), 404

    return jsonify(updated_user)


@ app.get('/api/users/<id>')  # obtener de a uno por uno
def get_user(id):

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM users WHERE id = %s', (id,))
    user = cur.fetchone()

    if user is None:
        return jsonify({'message': 'Usuario no encontrado'}), 404

    return jsonify(user)


@app.get('/')
def home():
    return send_file('static/index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
