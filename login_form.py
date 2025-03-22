from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')

    def validate_password(self, field):
        if len(field.data) < 8 :
            raise ValidationError('Password must have more then 8 characters')

    def validate_email(self, field):
        if "@"  not in field.data and "." not in field.data:
            raise ValidationError('Invalid Email')