from config import db


# Cargo
class Role(db.Model):
    __tablename__ = 'role'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Autoridade
    authority = db.Column(db.String(255), nullable=False)
    # Relacionamento com Usuário
    users = db.relationship("User")

    def to_json(self):
        return {
            'id': self.id,
            'authority': self.authority
        }

    def __str__(self):
        return f'Role:[ id: {self.id}, authority: {self.authority} ]'


# Notificação
class Notification(db.Model):
    __tablename__ = 'notification'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Texto
    text = db.Column(db.String(255), nullable=False)
    # Momento
    moment = db.Column(db.DateTime, nullable=False)
    # Lido
    read = db.Column(db.Boolean, unique=False, default=True)
    # Rota
    route = db.Column(db.String(255), nullable=False)
    # Usuário
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", back_populates="notifications")

    def to_json(self):
        return {
            'id': self.id,
            'text': self.text,
            'moment': self.moment,
            'read': self.read,
            'route': self.route,
            'userId': self.user_id
        }

    def __str__(self):
        return f'Notification:' \
               f'[ id: {self.id}, text: {self.text}, moment: {self.moment}, read: {self.read}, route: {self.route},' \
               f' userId: {self.user_id}] '


# Usuário
class User(db.Model):
    __tablename__ = 'user'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Nome
    name = db.Column(db.String(255), nullable=False)
    # E-mail
    email = db.Column(db.String(255), nullable=False)
    # Password
    password = db.Column(db.String(255), nullable=False)
    # Cargo
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False)
    # Notificações
    notifications = db.relationship("Notification", back_populates="user")
    # Tópicos
    topics = db.relationship("Topic")
    # Ofertas
    offers = db.relationship("Enrollment")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'roleId': self.role_id,
            'notifications': [notification.to_json() for notification in self.notifications]
        }

    def __str__(self):
        return f'User:[' \
               f' id: {self.id}, name: {self.name}, email: {self.email}, password: {self.password}, ' \
               f'roleId: {self.role_id}, ' \
               f'notifications: {self.notifications} ]'


# Curso
class Course(db.Model):
    __tablename__ = 'course'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Nome
    name = db.Column(db.String(255), nullable=False)
    # Endereço da imagem
    img_uri = db.Column(db.String(255), nullable=False)
    # Endereço da imagem quando concluído
    img_gray_uri = db.Column(db.String(255), nullable=False)
    # Ofertas
    offers = db.relationship("Offer", back_populates="course")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'imgUri': self.img_uri,
            "imgGrayUri": self.img_gray_uri,
            "offers": [offer.to_json() for offer in self.offers]
        }

    def __str__(self):
        string_return = f'Course:[ id: {self.id}, name: {self.name}, imgUri: {self.img_uri}, ' \
                        f'imgGrayUri: {self.img_gray_uri},' \
              f'offers: ['
        for offer in self.offers:
            string_return += str(offer.id) + ','
        string_return += '] ]'
        return string_return


# Oferta
class Offer(db.Model):
    __tablename__ = 'offer'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Edição
    edition = db.Column(db.String(255), nullable=False)
    # Data de início
    start_date = db.Column(db.Date, nullable=False)
    # Data de término
    end_date = db.Column(db.Date, nullable=False)
    # Curso
    course_id = db.Column(db.Integer, db.ForeignKey(Course.id), nullable=False)
    course = db.relationship("Course", back_populates="offers")
    # Disciplinas
    subjects = db.relationship("Subject", back_populates="offer")
    # Tópico
    topics = db.relationship("Topic", back_populates="offer")

    def to_json(self):
        return {
            'id': self.id,
            'edition': self.edition,
            'startDate': self.start_date,
            'endDate': self.end_date,
            'courseId': self.course_id,
            'subjects': [subject.to_json() for subject in self.subjects],
            'topics': [topic.to_json() for topic in self.topics]
        }

    def __str__(self):
        return f'Offer:' \
               f'[ id: {self.id}, edition: {self.edition}, startDate: {self.start_date}, endDate: {self.end_date}, ' \
               f'courseId: {self.course_id}, ' \
               f'subjects: {self.subjects},' \
               f'topics: {self.topics} ]'


# Inscrição
class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    # Usuário
    user_id = db.Column(db.ForeignKey(User.id), primary_key=True)
    # Oferta
    offer_id = db.Column(db.ForeignKey(Offer.id), primary_key=True)
    # Momento da inscrição
    enrollment = db.Column(db.DateTime, nullable=False)
    # Momento de pedido de reembolso
    refund_moment = db.Column(db.DateTime)
    # Disponível
    available = db.Column(db.Boolean, unique=False, default=True)
    # Apenas para atualização
    only_update = db.Column(db.Boolean)
    # Oferta
    offer = db.relationship("Offer")

    def to_json(self):
        return {
            'user_id': self.user_id,
            'offer_id': self.offer_id,
            'enrollment': self.enrollment,
            'refundMoment': self.refund_moment,
            'available': self.available,
            'onlyUpdate': self.only_update,
            'offer': self.offer
        }

    def __str__(self):
        return f'Enrollment:[' \
               f' user_id: {self.user_id}, offer_id: {self.offer_id}, enrollment: {self.enrollment}, ' \
               f'refundMoment: {self.refund_moment}, available: {self.available}, onlyUpdate: {self.only_update}, ' \
               f'offer: {self.offer} ]'


# Disciplina
class Subject(db.Model):
    __tablename__ = 'subject'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Título
    title = db.Column(db.String(255), nullable=False)
    # Descrição
    description = db.Column(db.String(3200), nullable=False)
    # Posição
    position = db.Column(db.Integer, nullable=False)
    # Link da imagem
    img_uri = db.Column(db.String(255), nullable=False)
    # Link externo
    external_link = db.Column(db.String(255))
    # Oferta
    offer_id = db.Column(db.Integer, db.ForeignKey(Offer.id), nullable=False)
    offer = db.relationship("Offer", back_populates="subjects")
    # Módulos
    modules = db.relationship("Module", back_populates="subject")

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'position': self.position,
            'imgUri': self.img_uri,
            'externalLink': self.external_link,
            'offerId': self.offer_id,
            'modules': [module.to_json() for module in self.modules]
        }

    def __str__(self):
        return f'Subject:' \
               f'[ id: {self.id}, title: {self.title}, description: {self.description}, position: {self.position}, ' \
               f' imgUri: {self.img_uri}, externalLink: {self.external_link}, ' \
               f'offerId: {self.offer_id}, ' \
               f'modules: {self.modules}]'


# Módulo
class Module(db.Model):
    __tablename__ = 'module'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Título
    title = db.Column(db.String(255), nullable=False)
    # Descrição
    description = db.Column(db.String(3200), nullable=False)
    # Posição
    position = db.Column(db.Integer, nullable=False)
    # Link da imagem
    img_uri = db.Column(db.String(255), nullable=False)
    # Disciplina
    subject_id = db.Column(db.Integer, db.ForeignKey(Subject.id), nullable=False)
    subject = db.relationship("Subject", back_populates="modules")
    # Lições
    lessons = db.relationship("Lesson", back_populates="module")

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'position': self.position,
            'imgUri': self.img_uri,
            'subjectId': self.subject_id,
            'lessons': [lesson.to_json() for lesson in self.lessons]
        }

    def __str__(self):
        return f'Module:' \
               f'[ id: {self.id}, title: {self.title}, description: {self.description}, position: {self.position}, ' \
               f' imgUri: {self.img_uri}, ' \
               f'subjectId: {self.subject_id}, ' \
               f'lessons: {self.lessons}]'


# Lição
class Lesson(db.Model):
    __tablename__ = 'lesson'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Título
    title = db.Column(db.String(255), nullable=False)
    # Posição
    position = db.Column(db.Integer, nullable=False)
    # Conteúdo textual
    text_content = db.Column(db.String(3200), nullable=False)
    # Link para vídeo-aula
    video_uri = db.Column(db.String(255), nullable=False)
    # Disciplina
    module_id = db.Column(db.Integer, db.ForeignKey(Module.id), nullable=False)
    module = db.relationship("Module", back_populates="lessons")
    # Tópico
    topics = db.relationship("Topic", back_populates="lesson")

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'position': self.position,
            'textContent': self.text_content,
            'videoUri': self.video_uri,
            'moduleId': self.module_id
        }

    def __str__(self):
        return f'Lesson:' \
               f'[ id: {self.id}, title: {self.title}, position: {self.position}, ' \
               f' textContent: {self.text_content}, videoUri: {self.video_uri}, ' \
               f'moduleId: {self.module_id}]'


user_likes_table = db.Table('user_like', db.Model.metadata,
                            db.Column('topic_id', db.ForeignKey('topic.id'), primary_key=True),
                            db.Column('user_id', db.ForeignKey('user.id'), primary_key=True)
                            )


# Tópico
class Topic(db.Model):
    __tablename__ = 'topic'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Título
    title = db.Column(db.String(255), nullable=False)
    # Corpo do texto
    body = db.Column(db.String(3200), nullable=False)
    # Momento
    moment = db.Column(db.DateTime, nullable=False)
    # Autor
    author_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    # Oferta
    offer_id = db.Column(db.Integer, db.ForeignKey(Offer.id), nullable=False)
    offer = db.relationship("Offer", back_populates="topics")
    # Lesson
    lesson_id = db.Column(db.Integer, db.ForeignKey(Lesson.id), nullable=False)
    lesson = db.relationship("Lesson", back_populates="topics")
    # Curtidas
    likes = db.relationship("User", secondary=user_likes_table)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'moment': self.moment,
            'authorId': self.author_id,
            'offerId': self.offer_id,
            'lesson_id': self.lesson_id,
            'likes': [like.to_json() for like in self.likes]
        }

    def __str__(self):
        return f'Topic:' \
               f'[ id: {self.id}, title: {self.title}, body: {self.body}, moment: {self.moment}, ' \
               f'authorId: {self.author_id}, ' \
               f'offerId: {self.offer_id}, ' \
               f'lessonId: {self.lesson_id}, ' \
               f'likes: {self.likes}] '
