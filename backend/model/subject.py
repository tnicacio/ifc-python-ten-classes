from config import db


# Disciplina
class Subject(db.Model):
    __tablename__ = 'subject'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Nome
    name = db.Column(db.String(255))
    # Carga horária
    workload = db.Column(db.Integer)
    # Ementa
    syllabus = db.Column(db.String(3200))
    # Pai no relacionamento One-To-Many com a entidade Student
    students = db.relationship("Student", back_populates="subject", cascade="all, delete-orphan")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'workload': self.workload,
            'syllabus': self.syllabus,
            'students': [student.to_json() for student in self.students]
        }

    def __str__(self):
        return f'Subject:[ id: {self.id}, name: {self.name}, workload: {self.workload}, syllabus: {self.syllabus} ]'
