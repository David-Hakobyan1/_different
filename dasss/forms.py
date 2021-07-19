from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

class RegisterForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired(),EqualTo(pass_confirm)])
    password_confirm = PasswordField('password confirm',validators=[DataRequired()])
    play = SubmitField("REGISTER")

class LoginForm(FlaskForm):
    email = StringField


