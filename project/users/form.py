from flask_wtf.form import Form
#from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(Form):
	username = TextField('Username', validators=[DataRequired(), Length(min=12, max=14)])







