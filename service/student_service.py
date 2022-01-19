from config import db
from model.student import Student
from flask import abort
from service.person_service import PersonService
from service.subject_service import SubjectService


class StudentService:

    @staticmethod
    def find_by_id(student_id):
        student_found = db.session.query(Student).filter(Student.id == student_id).one_or_none()
        if student_found is None:
            abort(404, f'Student not found with id {student_id}')
        return student_found

    @staticmethod
    def find_all():
        return db.session.query(Student).all()

    @staticmethod
    def insert(json_request):
        PersonService.find_by_id(json_request['person_id'])
        SubjectService.find_by_id(json_request['subject_id'])
        try:
            new_student = Student(semester=json_request['semester'],
                                  final_score=json_request['final_score'],
                                  frequency=json_request['frequency'],
                                  person_id=json_request['person_id'],
                                  subject_id=json_request['subject_id'])
            db.session.add(new_student)
            db.session.commit()
        except Exception as e:
            return {'error': str(e)}
        return new_student.to_json()

    @staticmethod
    def delete(student_id):
        student_found = db.session.query(Student).filter(Student.id == student_id).one_or_none()
        if student_found is None:
            abort(404, f'Student not found with id {student_id}')
        db.session.delete(student_found)
        db.session.commit()
