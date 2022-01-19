from flask import jsonify, request

from config import app
from service.person_service import PersonService


@app.route("/persons/<person_id>")
def find_person_by_id(person_id):
    person_found = PersonService.find_by_id(person_id)
    response = jsonify(person_found.to_json())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/persons")
def find_persons():
    person_name = request.args.get('name')

    persons = PersonService.find_all(person_name)
    persons_in_json = [p.to_json() for p in persons]
    response = jsonify(persons_in_json)
    
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/persons", methods=['post'])
def insert_person():
    new_person = PersonService.insert(request.get_json())
    if 'error' in new_person:
        return jsonify({"result": "error", "details": new_person['error']})
    
    response = jsonify(new_person)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/persons/<int:person_id>", methods=['DELETE'])
def delete_person(person_id):
    PersonService.delete(person_id)
    response = jsonify()
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
