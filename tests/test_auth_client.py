import re
import unittest
from app import create_app, db
from app.models import User


class FlaskClientTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Hello' in response.get_data(as_text=True))

    def test_register_and_login(self):
        # Fetch the regsiter page
        response = self.client.get('/auth/register')
        self.assertEqual(response.status_code, 200)

        # register a new account
        response = self.client.post('/auth/register', data={
            'email': 'dan@example.com',
            'username': 'dan',
            'password': 'pass',
            'password2': 'pass'
        })
        self.assertEqual(response.status_code, 302)

        # registering account with same username as other account
        response = self.client.post('/auth/register', data={
            'email': 'danny@example.com',
            'username': 'dan',
            'password': 'passss',
            'password2': 'passss'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(re.search('Username already in use',
                                  response.get_data(as_text=True)))

        # registering account with same email as other account
        response = self.client.post('/auth/register', data={
            'email': 'dan@example.com',
            'username': 'dan',
            'password': 'password',
            'password2': 'password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(re.search('Email already registered',
                                  response.get_data(as_text=True)))

        # login with the new account
        response = self.client.post('/auth/login', data={
            'email': 'dan@example.com',
            'password': 'pass'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(re.search('Hello,\s+dan!',
                                  response.get_data(as_text=True)))
        self.assertTrue(
            'You have not confirmed your account yet' in response.get_data(
                as_text=True))

        # send a confirmation token
        user = User.query.filter_by(email='dan@example.com').first()
        token = user.generate_confirmation_token()
        response = self.client.get('/auth/confirm/{}'.format(token),
                                   follow_redirects=True)
        user.confirm(token)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            'Hello' in response.get_data(
                as_text=True))

        # Resend confirmation
        user = User.query.filter_by(email='dan@example.com').first()
        response = self.client.get('/auth/confirm',
                                   follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            'Hello' in response.get_data(
                as_text=True))

        # Fetching the /unconfirmed route
        response = self.client.get('/auth/unconfirmed', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # login with unregistered account
        response = self.client.post('/auth/login', data={
            'email': 'unregistered@example.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            'Login' in response.get_data(
                as_text=True))

        # log out
        response = self.client.get('/auth/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Hello, Stranger!' in response.get_data(
            as_text=True))
