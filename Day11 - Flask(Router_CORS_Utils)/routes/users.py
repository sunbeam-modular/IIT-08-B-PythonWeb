from utils.util import crypto
from flask import Blueprint, request, jsonify
from flask_jwt_extended import (create_access_token)
import utils.db as db
from utils.util import createResult


usersRouter = Blueprint("users", __name__, url_prefix="/users")

@usersRouter.post("/signup")
def signup():
    sql = "INSERT INTO users(name, email, password, mobile) VALUES(%s, %s, %s, %s)"
    encPassword = crypto.hash(request.json["password"])
    params = (request.json["name"], request.json["email"], encPassword, request.json["mobile"])
    result = db.executeQuery(sql, params)
    return jsonify(result)

@usersRouter.post("/signin")
def signin():
    sql = "SELECT * FROM users WHERE email = %s"
    params = (request.json["email"], )
    result = db.executeQuery(sql, params)
    success = False
    if len(result) == 1:
        success = crypto.verify(request.json["password"], result[0]["password"])
    if not success or not result:
        return createResult("Invalid email or password", None)
    # return jsonify(result)
    jwt = create_access_token(identity=request.json["email"], expires_delta=False)
    result[0]["token"] = jwt
    return createResult(None, result[0])


