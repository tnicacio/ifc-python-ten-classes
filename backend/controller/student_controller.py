from flask import jsonify, request

from config import app
from service.student_service import StudentService


@app.route("/students/<student_id>")
def find_student_by_id(student_id):
    student_found = StudentService.find_by_id(student_id)
    response = jsonify(student_found.to_json())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/students")
def find_students():
    students = StudentService.find_all()
    students_in_json = [s.to_json() for s in students]
    response = jsonify(students_in_json)

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/students", methods=['post'])
def insert_student():
    new_student = StudentService.insert(request.get_json())
    if 'error' in new_student:
        return jsonify({"result": "error", "details": new_student['error']})

    response = jsonify(new_student)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/students/<int:student_id>", methods=['DELETE'])
def delete_student(student_id):
    StudentService.delete(student_id)
    response = jsonify()
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
