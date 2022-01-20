from flask import jsonify, request

from config import app
from service.role_service import RoleService


@app.route("/roles/<role_id>")
def find_role_by_id(role_id):
    role_found = RoleService.find_by_id(role_id)
    response = jsonify(role_found.to_json())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/roles")
def find_roles():
    roles = RoleService.find_all()
    roles_in_json = [role.to_json() for role in roles]
    response = jsonify(roles_in_json)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/roles", methods=['post'])
def insert_role():
    new_role = RoleService.insert(request.get_json())
    if 'error' in new_role:
        return jsonify({"result": "error", "details": new_role['error']})
    response = jsonify(new_role)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/roles/<int:role_id>", methods=['DELETE'])
def delete_role(role_id):
    RoleService.delete(role_id)
    response = jsonify()
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
