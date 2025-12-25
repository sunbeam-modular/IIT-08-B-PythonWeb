from flask import jsonify
from passlib.hash import sha256_crypt
from flask_jwt_extended import (JWTManager)

crypto = sha256_crypt

def createResult(error, data):
    if data:
        return jsonify(status="success", data=data)
    else: 
        return jsonify(status="error", error=error)

def enableJWT(app):
    app.config["JWT_SECRET_KEY"] = "secret-key"
    jwt = JWTManager(app)

    @jwt.unauthorized_loader
    def unauthorized_callback(callback):
        return createResult("Unauthorized", None), 200

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return createResult(f"Invalid token: {error}", None), 200
