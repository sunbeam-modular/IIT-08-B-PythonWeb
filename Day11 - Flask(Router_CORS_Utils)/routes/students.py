from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
import utils.db as db
from utils.util import createResult

studentsRouter = Blueprint("students", __name__, url_prefix="/students")

# Students REST apis - CRUD operations

# url: http://localhost:5000/students
@studentsRouter.get("/")
@jwt_required()
def getAllStudents():
    jwt_payload = get_jwt()
    print("Current User:", jwt_payload["sub"])
    sql = "SELECT * FROM students"
    result = db.executeQuery(sql, None)
    return createResult(None, result)


# url: http://localhost:5000/students/1
@studentsRouter.get("/<int:rollno>")
@jwt_required()
def getStudent(rollno):
    sql = "SELECT * FROM students WHERE rollno = %s"
    params = (rollno,)
    result = db.executeQuery(sql, params)
    return createResult(None, result)

# url: http://localhost:5000/students
# json body: {"name": "name", "email": "email", "course": "course"}
@studentsRouter.post("/")
@jwt_required()
def addStudent():
    sql = "INSERT INTO students(name, email, course) VALUES(%s, %s, %s)"
    params = (request.json["name"], request.json["email"], request.json["course"])
    result = db.executeQuery(sql, params)
    return createResult(None, result)

# url: http://localhost:5000/students/1
# json body: {"name": "name", "email": "email", "course": "course"}
@studentsRouter.put("/<int:rollno>")
@jwt_required()
def updateStudent(rollno):
    sql = "UPDATE students SET name = %s, email = %s, course = %s WHERE rollno = %s"
    params = (request.json["name"], request.json["email"], request.json["course"], rollno)
    result = db.executeQuery(sql, params)
    return createResult(None, result)

# delete operation using query string
# url: http://localhost:5000/students/?rollno=1
@studentsRouter.delete("/")
@jwt_required()
def deleteStudent():
    rollno = request.args.get("rollno")
    if rollno is None:
        return createResult("rollno is required", None)
    sql = "DELETE FROM students WHERE rollno = %s"
    params = (rollno,)
    result = db.executeQuery(sql, params)
    return createResult(None, result)
