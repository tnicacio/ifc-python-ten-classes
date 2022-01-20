from config import db
from flask import abort
from model.entities import User
from service.role_service import RoleService


class UserService:

    @staticmethod
    def find_by_id(user_id):
        user_found = db.session.query(User).filter(User.id == user_id).one_or_none()
        if user_found is None:
            abort(404, f'User not found with id {user_id}')
        return user_found

    @staticmethod
    def find_all(user_name=None):
        if user_name is not None:
            return db.session.query(User).filter(User.name.ilike('%' + user_name.lower() + '%')).all()
        else:
            return db.session.query(User).all()

    @staticmethod
    def insert(json_request):
        RoleService.find_by_id(json_request['roleId'])
        try:
            new_user = User(name=json_request['name'],
                            email=json_request['email'],
                            password=json_request['password'],
                            role_id=json_request['roleId'])
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            return {'error': str(e)}
        return new_user.to_json()

    @staticmethod
    def delete(user_id):
        user_found = db.session.query(User).filter(User.id == user_id).one_or_none()
        if user_found is None:
            abort(404, f'User not found with id {user_id}')
        db.session.delete(user_found)
        db.session.commit()
