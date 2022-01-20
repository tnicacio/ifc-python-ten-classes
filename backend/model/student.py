from config import db
from model.person import Person
from model.subject import Subject


# Estudante da disciplina
class Student(db.Model):
    __tablename__ = 'student'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Semestre
    semester = db.Column(db.Integer)
    # Média final
    final_score = db.Column(db.Float)
    # Frequência
    frequency = db.Column(db.Float)
    # Pessoa
    person_id = db.Column(db.Integer, db.ForeignKey(Person.id), nullable=False)
    # Disciplina
    subject_id = db.Column(db.Integer, db.ForeignKey(Subject.id), nullable=False)
    # Filho no relacionamento Many-To-One com a entidade Person
    # https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-one
    person = db.relationship("Person", back_populates="students")
    # Filho no relacionamento Many-To-One com a entidade Subject
    subject = db.relationship("Subject", back_populates="students")

    def to_json(self):
        return {
            'id': self.id,
            'semester': self.semester,
            'final_score': self.final_score,
            'frequency': self.frequency,
            'person_id': self.person_id,
            'subject_id': self.subject_id
        }

    def __str__(self):
        s = f'Student:[ id: {self.id}, semester: {self.semester}, final_score: {self.final_score}, '
        s += f'frequency: {self.frequency}, person: {self.person.to_json()}, subject: {self.subject.to_json()}] '
        return s


if __name__ == "__main__":
    try:
        import os
        from config import db, app

        root_dir = os.path.dirname(os.path.abspath(__file__))
        db_testing_classes = os.path.join(root_dir, 'test_classes.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_testing_classes

        if os.path.exists(db_testing_classes):
            os.remove(db_testing_classes)
        db.create_all()
    except Exception as e:
        print(f'Some modules are missing {e}')

    person1 = Person(name="Joaquina", cpf="08173948192")
    person2 = Person(name="Kevin", cpf="74829182013")
    subject1 = Subject(name="Matemática", workload=40, syllabus="Ementa da disciplina Matemática")
    subject2 = Subject(name="Inglês", workload=40, syllabus="Ementa de inglês")
    student1 = Student(semester=5, final_score=9.2, frequency=80.5, person_id=1, subject_id=1)
    student2 = Student(semester=4, final_score=9.5, frequency=90.1, person_id=2, subject_id=1)
    student3 = Student(semester=4, final_score=8.3, frequency=75.8, person_id=2, subject_id=2)

    db.session.add_all([person1, person2])
    db.session.add_all([subject1, subject2])
    db.session.add_all([student1, student2, student3])
    db.session.commit()

    print(person1)
    print(person2)
    print(subject1)
    print(subject2)
    print(student1)
    print(student2)
    print(student3)
