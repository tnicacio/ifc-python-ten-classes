from flask import jsonify, request

from config import app
from service.user_service import UserService


@app.route("/users/<user_id>")
def find_user_by_id(user_id):
    user_found = UserService.find_by_id(user_id)
    response = jsonify(user_found.to_json())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/users")
def find_users():
    user_name = request.args.get('name')

    users = UserService.find_all(user_name)
    users_in_json = [user.to_json() for user in users]
    response = jsonify(users_in_json)
    
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/users", methods=['post'])
def insert_user():
    new_user = UserService.insert(request.get_json())
    if 'error' in new_user:
        return jsonify({"result": "error", "details": new_user['error']})
    
    response = jsonify(new_user)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/users/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    UserService.delete(user_id)
    response = jsonify()
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
