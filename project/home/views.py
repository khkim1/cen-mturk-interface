from project import app, db
from project.models import BlogPost
from project.home.forms import MessageForm
from flask import render_template, Blueprint, flash, url_for, redirect, request
from flask_login import login_required, current_user
import os
import numpy as np

home_blueprint = Blueprint(
	'home', __name__,
	template_folder='templates'
)

numHITS_per_task = 10

# Routes 
@home_blueprint.route("/", methods=['GET', 'POST'])
@login_required
def home():
	error = None
	if current_user.name == "admin":
		posts = db.session.query(BlogPost).all()
		return render_template('index_admin.html', \
			posts=posts, error=error, username=current_user.name)

	else:
		all_posts = db.session.query(BlogPost).filter(BlogPost.author_id==current_user.id)
		num_hits = all_posts.count() // numHITS_per_task
		counter = 1
		posts = []
		for row in all_posts:
			if counter % numHITS_per_task == 0: 
				posts.append(row)
			counter += 1

		return render_template('index.html', \
			error=error, username=current_user.name,
			num_hits=num_hits, posts=posts)

@home_blueprint.route('/welcome')
def welcome(): 
	return render_template("welcome.html")




