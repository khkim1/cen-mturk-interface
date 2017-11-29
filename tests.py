from project import app, db
import unittest
from flask_testing import TestCase
from flask_login import current_user
from project.models import User, BlogPost


class BaseTestCase(TestCase):

	def create_app(self): 
		app.config.from_object('config.TestConfig')
		return app

	def setUp(self):
		db.create_all()
		db.session.add(User("admin", "ad@min.com", "admin"))
		db.session.add(BlogPost("Test post", 
			"This is a test. Only a test.", 
			"admin"))
		db.session.commit()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

class FlaskTestCase(BaseTestCase):

	# Flask setup check 
	def test_index(self): 
		response = self.client.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	# Main page login required check 
	def test_main_route_requires_login(self): 
		response = self.client.get('/', follow_redirects=True)
		self.assertIn(b'Please log in to access this page.', response.data)

	# Main page post show up check 
	def test_post_show_up(self): 
		response = self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
		self.assertIn(b'This is a test. Only a test.', response.data)

class UsersViewsTests(BaseTestCase):

	# Login page load check 
	def test_login_page_loads(self):
		response = self.client.get('/login', content_type='html/text')
		self.assertTrue(b'Please login' in response.data)

	# Login page credential check 
	def test_correct_login(self): 
		with self.client:
			response = self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
			self.assertIn(b'You were logged in', response.data)
			self.assertTrue(current_user.name == "admin")
			self.assertTrue(current_user.is_active())

	# Login page incorrect credentials check 
	def test_incorrect_login(self): 
		response = self.client.post('/login', data=dict(username="wrong", password="wrong"), follow_redirects=True)
		self.assertIn(b'Invalid credentials. Please try again.', response.data)

	# Logout check 
	def test_logout(self): 
		with self.client:
			self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
			response = self.client.get('/logout', follow_redirects=True)
			self.assertIn(b'You were logged out', response.data)
			self.assertFalse(current_user.is_active())

	# Main page login required check 
	def test_logout_route_requires_login(self): 
		response = self.client.get('/logout', follow_redirects=True)
		self.assertIn(b'Please log in to access this page.', response.data)

	# Ensure user can register 
	def test_user_registeration(self): 
		with self.client:
			response = self.client.post('/register', \
				data=dict(username="Michael", email="john123@gmail.com", password="michael", confirm="michael"), \
				follow_redirects=True)
			self.assertIn(b'Your HIT', response.data)
			self.assertTrue(current_user.name == "Michael")
			self.assertTrue(current_user.is_active())

if __name__ == '__main__': 
	unittest.main()