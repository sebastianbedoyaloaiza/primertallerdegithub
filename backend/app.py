from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #Esto es para permitir las peticiones desde Vue 

#Datos simulados (base de datos) 
users = []

# Ruta de registro 
@app.route("/register", methods=["POST"])
def register(): 
    data = request.json
    email = data.get("email")
    password = data.get("password")

# Verificar si ya existe
    for u in users:
        if u["email"] == email:
            return jsonify({"message": "Usuario ya existe"}), 400

    # Guardar
    users.append({"email": email, "password": password})
    return jsonify({"message": "Registro exitoso"}), 201
# Ruta de login
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    # Validación contra el usuario de prueba
    if email == "user@test.com" and password == "Test123":
        return jsonify({"message": "Inicio de sesión exitoso (usuario de prueba)"}), 200

    # Validación contra usuarios registrados
    for u in users:
        if u["email"] == email and u["password"] == password:
            return jsonify({"message": "Inicio de sesión exitoso"}), 200

    return jsonify({"message": "Credenciales inválidas"}), 401


if __name__ == "__main__":
    app.run(debug=True, port=5000)



