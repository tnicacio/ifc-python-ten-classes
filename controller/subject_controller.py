from flask import jsonify, request

from config import app
from service.subject_service import SubjectService


@app.route("/subjects/<subject_id>")
def find_subject_by_id(subject_id):
    subject_found = SubjectService.find_by_id(subject_id)
    response = jsonify(subject_found.to_json())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/subjects")
def find_subjects():
    subject_name = request.args.get('name')

    subjects = SubjectService.find_all(subject_name)
    subjects_in_json = [s.to_json() for s in subjects]
    response = jsonify(subjects_in_json)

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/subjects", methods=['post'])
def insert_subject():
    new_subject = SubjectService.insert(request.get_json())
    if 'error' in new_subject:
        return jsonify({"result": "error", "details": new_subject['error']})

    response = jsonify(new_subject)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/subjects/<int:subject_id>", methods=['DELETE'])
def delete_subject(subject_id):
    SubjectService.delete(subject_id)
    response = jsonify()
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
