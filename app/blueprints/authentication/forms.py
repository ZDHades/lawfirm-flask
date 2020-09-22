from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, EqualTo, email_validator
from flask_wtf import FlaskForm

# form that can be used on register and for a settings/profile page
class FullForm(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    email = StringField(validators=[Email(message='Not a valid email address')])
    password = PasswordField()
    confirm_password = PasswordField(EqualTo('password'))
    submit = SubmitField('Submit')

# form that can be used on login page
class LoginForm(FlaskForm):
    email = StringField(validators=[Email(message='Not a valid email address')])
    password = PasswordField()
    submit = SubmitField('Submit')