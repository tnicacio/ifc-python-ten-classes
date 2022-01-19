try:
    import os
    import json
    import unittest

    from config import app, root_dir, db
    from controller import *

    db_testing_file = os.path.join(root_dir, 'test_database.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_testing_file

    if os.path.exists(db_testing_file):
        os.remove(db_testing_file)
    db.create_all()

except Exception as e:
    print(f'Some modules are missing {e}')


class TestConstants:
    APPLICATION_JSON = 'application/json'
    PERSONS_ROUTE = '/persons'
    SUBJECTS_ROUTE = '/subjects'
    STUDENTS_ROUTE = '/students'


class PersonTest(unittest.TestCase):

    def test_get_persons_should_return_status_code_200(self):
        tester = app.test_client(self)

        response = tester.get(TestConstants.PERSONS_ROUTE)

        self.assertEqual(response.status_code, 200)

    def test_get_persons_should_return_content_type_application_json(self):
        tester = app.test_client(self)

        response = tester.get(TestConstants.PERSONS_ROUTE)

        self.assertEqual(response.content_type, TestConstants.APPLICATION_JSON)

    def test_post_persons_should_insert_person(self):
        tester = app.test_client(self)
        send = {'name': 'Luiza Maria', 'cpf': '89203928105'}

        response = tester.post(TestConstants.PERSONS_ROUTE, data=json.dumps(send),
                               headers={'Content-Type': TestConstants.APPLICATION_JSON})

        self.assertTrue(b'Luiza Maria' in response.data)
        self.assertTrue(b'89203928105' in response.data)

    def test_get_persons_should_return_inserted_person(self):
        tester = app.test_client(self)
        send = {'name': 'Maria de Fatima', 'cpf': '12303928105'}
        tester.post(TestConstants.PERSONS_ROUTE, data=json.dumps(send),
                    headers={'Content-Type': TestConstants.APPLICATION_JSON})

        response = tester.get(TestConstants.PERSONS_ROUTE)

        self.assertTrue(b'Maria de Fatima' in response.data)
        self.assertTrue(b'12303928105' in response.data)


class SubjectTest(unittest.TestCase):

    def test_get_subjects_should_return_status_code_200(self):
        tester = app.test_client(self)

        response = tester.get(TestConstants.SUBJECTS_ROUTE)

        self.assertEqual(response.status_code, 200)

    def test_get_subjects_should_return_content_type_application_json(self):
        tester = app.test_client(self)

        response = tester.get(TestConstants.SUBJECTS_ROUTE)

        self.assertEqual(response.content_type, TestConstants.APPLICATION_JSON)

    def test_post_subjects_should_insert_subject(self):
        tester = app.test_client(self)
        send = {
            "name": "Calculo 3",
            "workload": 60,
            "syllabus": "Derivadas, Integrais, Mais Curvas Legais"
        }

        response = tester.post(TestConstants.SUBJECTS_ROUTE, data=json.dumps(send),
                               headers={'Content-Type': TestConstants.APPLICATION_JSON})

        self.assertTrue(b'Calculo 3' in response.data)
        self.assertTrue(b'60' in response.data)
        self.assertTrue(b'Derivadas, Integrais, Mais Curvas Legais' in response.data)

    def test_get_subjects_should_return_inserted_subject(self):
        tester = app.test_client(self)
        send = {
            "name": "Empreendedorismo",
            "workload": 30,
            "syllabus": "Coisas de empreendedores"
        }
        tester.post(TestConstants.SUBJECTS_ROUTE, data=json.dumps(send),
                    headers={'Content-Type': TestConstants.APPLICATION_JSON})

        response = tester.get(TestConstants.SUBJECTS_ROUTE)

        self.assertTrue(b'Empreendedorismo' in response.data)
        self.assertTrue(b'30' in response.data)
        self.assertTrue(b'Coisas de empreendedores' in response.data)


class StudentTest(unittest.TestCase):

    def test_get_students_should_return_status_code_200(self):
        tester = app.test_client(self)

        response = tester.get(TestConstants.STUDENTS_ROUTE)

        self.assertEqual(response.status_code, 200)

    def test_get_students_should_return_content_type_application_json(self):
        tester = app.test_client(self)

        response = tester.get(TestConstants.STUDENTS_ROUTE)

        self.assertEqual(response.content_type, TestConstants.APPLICATION_JSON)

    def test_post_students_should_insert_student(self):
        tester = app.test_client(self)

        send_person = {'name': 'Maria Luiza', 'cpf': '89203928105'}
        person_response = tester.post(TestConstants.PERSONS_ROUTE, data=json.dumps(send_person),
                                      headers={'Content-Type': TestConstants.APPLICATION_JSON})

        send_subject = {
            "name": "Calculo 1",
            "workload": 60,
            "syllabus": "Algoritmos, Logaritmos, Derivadas"
        }
        subject_response = tester.post(TestConstants.SUBJECTS_ROUTE, data=json.dumps(send_subject),
                                       headers={'Content-Type': TestConstants.APPLICATION_JSON})

        person_id = person_response.get_json()['id']
        subject_id = subject_response.get_json()['id']
        send_student = {
            "semester": 6,
            "final_score": 9.5,
            "frequency": 78.82,
            "person_id": person_id,
            "subject_id": subject_id
        }
        response = tester.post(TestConstants.STUDENTS_ROUTE, data=json.dumps(send_student),
                               headers={'Content-Type': TestConstants.APPLICATION_JSON})

        self.assertTrue(b'6' in response.data)
        self.assertTrue(b'9.5' in response.data)
        self.assertTrue(b'78.82' in response.data)
        self.assertTrue(bytes(str(person_id), encoding='utf-8') in response.data)
        self.assertTrue(bytes(str(subject_id), encoding='utf-8') in response.data)

    def test_get_students_should_return_inserted_student(self):
        tester = app.test_client(self)

        send_person = {'name': 'Maria Luiza', 'cpf': '89203928105'}
        person_response = tester.post(TestConstants.PERSONS_ROUTE, data=json.dumps(send_person),
                                      headers={'Content-Type': TestConstants.APPLICATION_JSON})

        send_subject = {
            "name": "Calculo 1",
            "workload": 60,
            "syllabus": "Algoritmos, Logaritmos, Derivadas"
        }
        subject_response = tester.post(TestConstants.SUBJECTS_ROUTE, data=json.dumps(send_subject),
                                       headers={'Content-Type': TestConstants.APPLICATION_JSON})

        person_id = person_response.get_json()['id']
        subject_id = subject_response.get_json()['id']
        send_student = {
            "semester": 4,
            "final_score": 9.3,
            "frequency": 78.22,
            "person_id": person_id,
            "subject_id": subject_id
        }
        tester.post('/students', data=json.dumps(send_student),
                    headers={'Content-Type': TestConstants.APPLICATION_JSON})

        response = tester.get(TestConstants.STUDENTS_ROUTE)

        self.assertTrue(b'4' in response.data)
        self.assertTrue(b'9.3' in response.data)
        self.assertTrue(b'78.22' in response.data)
        self.assertTrue(bytes(str(person_id), encoding='utf-8') in response.data)
        self.assertTrue(bytes(str(subject_id), encoding='utf-8') in response.data)


if __name__ == '__main__':
    unittest.main()
