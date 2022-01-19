from config import db
from model.subject import Subject
from flask import abort


class SubjectService:

    @staticmethod
    def find_by_id(subject_id):
        subject_found = db.session.query(Subject).filter(Subject.id == subject_id).one_or_none()
        if subject_found is None:
            abort(404, f'Subject not found with id {subject_id}')
        return subject_found

    @staticmethod
    def find_all(subject_name=None):
        if subject_name is not None:
            return db.session.query(Subject).filter(Subject.name.ilike('%' + subject_name.lower() + '%')).all()
        else:
            return db.session.query(Subject).all()

    @staticmethod
    def insert(json_request):
        try:
            new_subject = Subject(name=json_request['name'],
                                  workload=json_request['workload'],
                                  syllabus=json_request['syllabus'])
            db.session.add(new_subject)
            db.session.commit()
        except Exception as e:
            return {'error': str(e)}
        return new_subject.to_json()

    @staticmethod
    def delete(subject_id):
        subject_found = db.session.query(Subject).filter(Subject.id == subject_id).one_or_none()
        if subject_found is None:
            abort(404, f'Subject not found with id {subject_id}')
        db.session.delete(subject_found)
        db.session.commit()
