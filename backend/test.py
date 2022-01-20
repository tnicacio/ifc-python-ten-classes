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
    USERS_ROUTE = '/users'
    ROLES_ROUTE = '/roles'


class UserTest(unittest.TestCase):

    def test_get_users_should_return_status_code_200(self):
        tester = app.test_client(self)
        response = tester.get(TestConstants.USERS_ROUTE)
        self.assertEqual(response.status_code, 200)

    def test_get_users_should_return_content_type_application_json(self):
        tester = app.test_client(self)
        response = tester.get(TestConstants.USERS_ROUTE)
        self.assertEqual(response.content_type, TestConstants.APPLICATION_JSON)

    def test_post_users_should_insert_user(self):
        tester = app.test_client(self)
        send_role = {'authority': 'ADMIN'}
        role_response = tester.post(TestConstants.ROLES_ROUTE, data=json.dumps(send_role),
                                    headers={'Content-Type': TestConstants.APPLICATION_JSON})
        role_id = role_response.get_json()['id']
        send_user = {'name': 'Luiza Maria', 'email': 'email@mail.com', 'password': '123456', 'roleId': role_id}
        response = tester.post(TestConstants.USERS_ROUTE, data=json.dumps(send_user),
                               headers={'Content-Type': TestConstants.APPLICATION_JSON})

        self.assertTrue(b'Luiza Maria' in response.data)
        self.assertTrue(b'email@mail.com' in response.data)
        self.assertTrue(b'123456' in response.data)
        self.assertTrue(bytes(str(role_id), encoding='utf-8') in response.data)

    def test_get_users_should_return_inserted_user(self):
        tester = app.test_client(self)
        send_role = {'authority': 'ADMIN'}
        role_response = tester.post(TestConstants.ROLES_ROUTE, data=json.dumps(send_role),
                                    headers={'Content-Type': TestConstants.APPLICATION_JSON})
        role_id = role_response.get_json()['id']
        send_user = {'name': 'Luiza Maria', 'email': 'email@mail.com', 'password': '123456', 'roleId': role_id}
        tester.post(TestConstants.USERS_ROUTE, data=json.dumps(send_user),
                               headers={'Content-Type': TestConstants.APPLICATION_JSON})

        response = tester.get(TestConstants.USERS_ROUTE)

        self.assertTrue(b'Luiza Maria' in response.data)
        self.assertTrue(b'email@mail.com' in response.data)
        self.assertTrue(b'123456' in response.data)
        self.assertTrue(bytes(str(role_id), encoding='utf-8') in response.data)


class RoleTest(unittest.TestCase):

    def test_get_roles_should_return_status_code_200(self):
        tester = app.test_client(self)
        response = tester.get(TestConstants.ROLES_ROUTE)
        self.assertEqual(response.status_code, 200)

    def test_get_roles_should_return_content_type_application_json(self):
        tester = app.test_client(self)
        response = tester.get(TestConstants.ROLES_ROUTE)
        self.assertEqual(response.content_type, TestConstants.APPLICATION_JSON)

    def test_post_roles_should_insert_role(self):
        tester = app.test_client(self)
        send_role = {'authority': 'ADMIN'}
        role_response = tester.post(TestConstants.ROLES_ROUTE, data=json.dumps(send_role),
                                       headers={'Content-Type': TestConstants.APPLICATION_JSON})
        self.assertTrue(b'ADMIN' in role_response.data)

    def test_get_roles_should_return_inserted_role(self):
        tester = app.test_client(self)
        send_role = {'authority': 'ADMIN'}
        tester.post(TestConstants.ROLES_ROUTE, data=json.dumps(send_role),
                                    headers={'Content-Type': TestConstants.APPLICATION_JSON})
        response = tester.get(TestConstants.ROLES_ROUTE)
        self.assertTrue(b'ADMIN' in response.data)


if __name__ == '__main__':
    unittest.main()
