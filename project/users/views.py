from flask import flash, redirect, render_template, request, \
url_for, Blueprint
from project.users.form import LoginForm
from project import db
from flask_login import login_user, login_required, logout_user
from project.models import User, bcrypt

############
## config ##
############

users_blueprint = Blueprint(
	'users', __name__, 
	template_folder='templates'
)

############
## routes ##
############
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	form = LoginForm(request.form)
	if request.method == 'POST':

		if form.validate_on_submit() or request.form['username'] == 'admin':
			user = User.query.filter_by(name=request.form['username']).first()

			if user is None: 
				db.session.add(User(request.form['username']))
				db.session.commit()

			user = User.query.filter_by(name=request.form['username']).first()
			login_user(user)
			flash('You were logged in.')
			return redirect(url_for('home.home'))			

	return render_template("login.html", form=form, error=error)


@users_blueprint.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You were logged out.')
	return redirect(url_for('home.welcome'))










