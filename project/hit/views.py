from project import app, db
from project.models import BlogPost
from project.hit.forms import ClusterForm
from flask import render_template, Blueprint, flash, url_for, redirect, request
from flask_login import login_required, current_user, session
import random
import os
import string
from werkzeug.routing import BaseConverter

hit_blueprint = Blueprint(
	'hit', __name__,
	template_folder='templates'
)

import re
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

full_img_names = os.listdir('./images')
# remove any non image files in the dir
for f in full_img_names:
	if f[0] == ".":
		full_img_names.remove(f);

key_length = 10 
numHITS_per_task = 10
num_images = 24
#cur_image_names = None

# Routes 
@hit_blueprint.route("/hit", methods=['GET', 'POST'])
@login_required
def hit():

	error = None
	form = ClusterForm(request.form)

	posts = db.session.query(BlogPost).filter(BlogPost.author_id==current_user.id)
	num_current_hits = posts.count() % numHITS_per_task

	if request.method == 'GET':
		cur_image_names = random.sample(full_img_names, num_images)
		session['cur_image_names'] = cur_image_names
		print("ON SCREEN")
		print(cur_image_names)
		return render_template('hitIndex.html', form=form, image_names=cur_image_names, hit_number=num_current_hits)
	
	else:
		cur_image_names = session['cur_image_names']

		# Retrieve the image names with .png removed upon submission 
		image_id = request.form['image_id_data']
		image_id = image_id.replace('[',"")
		image_id = image_id.replace(']',"")
		image_id = image_id.replace('"',"")

		#Retrieve the cluster ids upon submission 
		cluster_id = request.form['cluster_id_data']
		cluster_id = cluster_id.replace('[',"")
		cluster_id = cluster_id.replace(']',"")

		# Retrieve the group descriptions upon submission 
		group_descriptions = request.form['group_description_data']
		group_descriptions = group_descriptions.replace('[',"")
		group_descriptions = group_descriptions.replace(']',"")
		group_descriptions = group_descriptions.replace('"',"")

		#print("SUBMISSION")
		#print(image_id)
		#print(cluster_id)
		#print(group_descriptions)

		if num_current_hits == 0: 
			secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(key_length))
		else: 
			secret_key = str(posts[-1].secret_key)

		new_entry = BlogPost(image_id, cluster_id, group_descriptions, secret_key, current_user.id) 
		db.session.add(new_entry)
		db.session.commit()



		'''
		if num_current_hits + 1 != numHITS_per_task: 
			return redirect(url_for('hit.hit'))

		flash("Thank you for your submission.")
		return redirect(url_for('home.home'))
		'''










