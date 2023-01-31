from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from puppycompangblog.models import User

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_conf','Passwords must match !')])
    password_conf = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This E-mail is already used !')
        
    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This E-mail is already used !')
        
class UpdateUserForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This E-mail is already used !')
        
    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This E-mail is already used !')