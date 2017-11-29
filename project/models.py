from project import db
from project import bcrypt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin


class BlogPost(db.Model):
	
	__tablename__ = 'posts'

	id = db.Column(db.Integer, primary_key=True)
	image_id = db.Column(db.String, nullable=False)
	cluster_id = db.Column(db.String, nullable=False)
	group_descriptions = db.Column(db.String, nullable=False)
	secret_key = db.Column(db.String, nullable=False)
	author_id = db.Column(db.Integer, ForeignKey('users.id'))

	def __init__(self, image_id, cluster_id, group_descriptions, secret_key, author_id):
		self.image_id = image_id
		self.cluster_id = cluster_id
		self.group_descriptions = group_descriptions
		self.secret_key = secret_key
		self.author_id = author_id

	def __repr__(self):
		return '<{}>'.format(self.secret_key)

class User(db.Model, UserMixin):

	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	posts = relationship("BlogPost", backref="author")

	def __init__(self, name):
		self.name = name
		
	def is_authenticated(self):
		return True

	def is_active(self): 
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)

	def __repr__(self):
		return '<name {}'.format(self.name)








