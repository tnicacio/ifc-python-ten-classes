from config import db
from model.entities import Role
from flask import abort


class RoleService:

    @staticmethod
    def find_by_id(role_id):
        role_found = db.session.query(Role).filter(Role.id == role_id).one_or_none()
        if role_found is None:
            abort(404, f'Role not found with id {role_id}')
        return role_found

    @staticmethod
    def find_all():
        return db.session.query(Role).all()

    @staticmethod
    def insert(json_request):
        try:
            new_role = Role(authority=json_request['authority'])
            db.session.add(new_role)
            db.session.commit()
        except Exception as e:
            return {'error': str(e)}
        return new_role.to_json()

    @staticmethod
    def delete(role_id):
        role_found = db.session.query(Role).filter(Role.id == role_id).one_or_none()
        if role_found is None:
            abort(404, f'Student not found with id {role_id}')
        db.session.delete(role_found)
        db.session.commit()
