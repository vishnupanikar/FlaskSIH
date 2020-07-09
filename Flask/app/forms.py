from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email

class LoginForm(FlaskForm):
      email = StringField('Email', validators=[DataRequired()])
      password = PasswordField('Password', validators=[DataRequired()])
      remember_me = BooleanField('Remember Me')
      submit = SubmitField('Sign In')

class Register(FlaskForm):
      username = StringField('Username', validators=[DataRequired()])
      email = StringField('Email',validators=[DataRequired(),Email()])
      password = PasswordField('Password', validators=[DataRequired()])
      confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
      submit = SubmitField('Register')
