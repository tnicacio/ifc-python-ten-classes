from config import db
from flask import abort
from model.person import Person


class PersonService:

    @staticmethod
    def find_by_id(person_id):
        person_found = db.session.query(Person).filter(Person.id == person_id).one_or_none()
        if person_found is None:
            abort(404, f'Person not found with id {person_id}')
        return person_found

    @staticmethod
    def find_all(person_name=None):
        if person_name is not None:
            return db.session.query(Person).filter(Person.name.ilike('%' + person_name.lower() + '%')).all()
        else:
            return db.session.query(Person).all()

    @staticmethod
    def insert(json_request):
        try:
            new_person = Person(name=json_request['name'], cpf=json_request['cpf'])
            db.session.add(new_person)
            db.session.commit()
        except Exception as e:
            return {'error': str(e)}
        return new_person.to_json()

    @staticmethod
    def delete(person_id):
        person_found = db.session.query(Person).filter(Person.id == person_id).one_or_none()
        if person_found is None:
            print('abc')
        db.session.delete(person_found)
        db.session.commit()
