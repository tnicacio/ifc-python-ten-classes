if __name__ == "__main__":
    try:
        import os
        from datetime import datetime, timedelta
        from config import db, app
        from model.entities import *

        root_dir = os.path.dirname(os.path.abspath(__file__))
        db_testing_classes = os.path.join(root_dir, 'test_entities.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_testing_classes

        if os.path.exists(db_testing_classes):
            os.remove(db_testing_classes)
        db.create_all()
    except Exception as e:
        print(f'Some modules are missing {e}')

    # Test Role
    role_admin = Role(authority="ADMIN")
    role_instructor = Role(authority="INSTRUCTOR")
    role_student = Role(authority="STUDENT")
    db.session.add_all([role_admin, role_instructor, role_student])
    db.session.commit()

    # Test User
    user_joaquina = User(name="Joaquina", email="joaquina@email.com", password="123456", role_id=3)
    user_kevin = User(name="Kevin", email="kevin@email.com", password="123abc", role_id=1)
    db.session.add_all([user_joaquina, user_kevin])
    db.session.commit()

    # Test Notification
    notification_1 = Notification(text="Texto da primeira notificação", moment=datetime.utcnow(),
                                  read=False, route="www.ww.w", user_id=user_joaquina.id)
    notification_2 = Notification(text="Texto da segunda notificação já visualiizada ",
                                  moment=datetime.utcnow(),
                                  route="www.ww.w", user_id=user_kevin.id)
    db.session.add_all([notification_1, notification_2])
    db.session.commit()

    # Test Course
    course_engineering = Course(name="Engineering", img_uri="image uri", img_gray_uri="gray image uri")
    db.session.add(course_engineering)
    db.session.commit()

    # Test Offer
    offer_2021 = Offer(edition="1st", start_date=datetime.today() + timedelta(days=-365), end_date=datetime.max,
                       course_id=course_engineering.id)
    offer_2022 = Offer(edition="2nd", start_date=datetime.today(), end_date=datetime.max,
                       course_id=course_engineering.id)
    db.session.add_all([offer_2021, offer_2022])
    db.session.commit()

    # Test Enrollment
    enrollment_1 = Enrollment(user_id=user_joaquina.id, offer_id=offer_2021.id,
                              enrollment=datetime.today() + timedelta(days=-364))
    db.session.add(enrollment_1)
    db.session.commit()

    # Test Subject
    subject_math = Subject(title="Math", description="Math 101", position=1, img_uri="image_uri",
                           offer_id=offer_2021.id)
    subject_calculus = Subject(title="Calculus", description="Fun with Calculus", position=2, img_uri="image_uri_calc",
                               offer_id=offer_2021.id)
    db.session.add_all([subject_math, subject_calculus])
    db.session.commit()

    # Test Module
    module_1_math = Module(title="Arabic numbers", description="A bit of history", position=1,
                           img_uri="image_uri_arabic_numbers", subject_id=subject_math.id)
    module_1_calculus = Module(title="Limits", description="No limit", position=1,
                               img_uri="image_uri_limits_or_not", subject_id=subject_calculus.id)
    db.session.add_all([module_1_math, module_1_calculus])
    db.session.commit()

    # Test Lesson
    lesson_1_module_1_math = Lesson(title="Counting in arabic", position=1, text_content="Some content",
                                    video_uri="video_uri_l1_m1_math", module_id=module_1_math.id)
    db.session.add(lesson_1_module_1_math)
    db.session.commit()

    # Test Topic
    topic_1 = Topic(title="What is it?", body="Some body", moment=datetime.today(), author_id=user_kevin.id,
                    offer_id=offer_2021.id, lesson_id=lesson_1_module_1_math.id)
    db.session.add(topic_1)
    db.session.commit()

    print(role_admin)
    print(role_instructor)
    print(role_student)
    print(user_joaquina)
    print(user_kevin)
    print(notification_1)
    print(notification_2)

    print(offer_2021)
    print(offer_2022)
    print(course_engineering)
    print(topic_1)

    print(lesson_1_module_1_math)
    print(module_1_math)
    print(module_1_calculus)
    print(subject_math)
    print(subject_calculus)
    print(enrollment_1)
