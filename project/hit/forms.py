from flask_wtf.form import Form
#from flask_wtf import Form
from wtforms import TextField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class ClusterForm(Form):

	num_clusters = 5

	image_11 = SelectField('image_11', \
		choices=[(str(i), str(i)) for i in range(num_clusters)], \
		validators=[DataRequired()])

	image_12 = SelectField('image_12', \
		choices=[(str(i), str(i)) for i in range(num_clusters)], \
		validators=[DataRequired()])

	image_13 = SelectField('image_13', \
		choices=[(str(i), str(i)) for i in range(num_clusters)], \
		validators=[DataRequired()])

	image_14 = SelectField('image_14', \
	choices=[(str(i), str(i)) for i in range(num_clusters)], \
	validators=[DataRequired()])

	image_21 = SelectField('image_21', \
		choices=[(str(i), str(i)) for i in range(num_clusters)], \
		validators=[DataRequired()])

	image_22 = SelectField('image_22', \
		choices=[(str(i), str(i)) for i in range(num_clusters)], \
		validators=[DataRequired()])

	image_23 = SelectField('image_23', \
		choices=[(str(i), str(i)) for i in range(num_clusters)], \
		validators=[DataRequired()])

	image_24 = SelectField('image_24', \
	choices=[(str(i), str(i)) for i in range(num_clusters)], \
	validators=[DataRequired()])

	image_31 = SelectField('image_31', \
		choices=[(str(i), str(i)) for i in range(num_clusters)], \
		validators=[DataRequired()])

	image_32 = SelectField('image_32', \
		choices=[(str(i), str(i)) for i in range(num_clusters)], \
		validators=[DataRequired()])

	image_33 = SelectField('image_33', \
		choices=[(str(i), str(i)) for i in range(num_clusters)], \
		validators=[DataRequired()])

	image_34 = SelectField('image_34', \
		choices=[(str(i), str(i)) for i in range(num_clusters)], \
		validators=[DataRequired()])

	image_41 = SelectField('image_41', \
		choices=[(str(i), str(i)) for i in range(num_clusters)], \
		validators=[DataRequired()])

	image_42 = SelectField('image_42', \
		choices=[(str(i), str(i)) for i in range(num_clusters)], \
		validators=[DataRequired()])

	image_43 = SelectField('image_43', \
		choices=[(str(i), str(i)) for i in range(num_clusters)], \
		validators=[DataRequired()])

	image_44 = SelectField('image_44', \
		choices=[(str(i), str(i)) for i in range(num_clusters)], \
		validators=[DataRequired()])








