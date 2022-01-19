from config import db


# Pessoa
class Person(db.Model):
    __tablename__ = 'person'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Nome
    name = db.Column(db.String(255))
    # CPF
    cpf = db.Column(db.String(11))
    # Pai no relacionamento One-To-Many com a entidade Student
    # https://docs.sqlalchemy.org/en/14/errors.html#for-relationship-relationship-delete-orphan-cascade-is-normally-configured-only-on-the-one-side-of-a-one-to-many-relationship-and-not-on-the-many-side-of-a-many-to-one-or-many-to-many-relationship
    students = db.relationship("Student", back_populates="person", cascade="all, delete-orphan")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'cpf': self.cpf
        }

    def __str__(self):
        return f'Person:[ id: {self.id}, name: {self.name}, cpf: {self.cpf} ]'
