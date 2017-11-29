# tests/test_models.py

import unittest

from flask_login import current_user
from base import BaseTestCase
from project import bcrypt
from project.models import User

class TestUser(BaseTestCase):
	pass


if __name__ == '__main__':
	unittest.main()