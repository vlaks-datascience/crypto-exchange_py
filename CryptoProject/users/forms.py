from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TelField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from CryptoProject.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=2, max=25)])
    surname = StringField('Surname',
                          validators=[DataRequired(), Length(min=2, max=30)])
    address = StringField('Address',
                          validators=[DataRequired(), Length(min=6, max=60)])
    city = StringField('City',
                       validators=[DataRequired(), Length(min=2, max=25)])
    state = StringField('Country',
                        validators=[DataRequired(), Length(min=2, max=25)])
    cellphone = TelField('Cellphone',
                         validators=[DataRequired(), Length(min=9, max=30)])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

    def validate_cellphone(self, cellphone):
        if not cellphone.data.isdigit():
            raise ValidationError('Cellphone needs to be in digit form!')
        else:
            user = User.query.filter_by(cellphone=cellphone.data).first()
            if user:
                raise ValidationError('That cellphone is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=2, max=25)])
    surname = StringField('Surname',
                          validators=[DataRequired(), Length(min=2, max=30)])
    address = StringField('Address',
                          validators=[DataRequired(), Length(min=6, max=60)])
    city = StringField('City',
                       validators=[DataRequired(), Length(min=2, max=25)])
    state = StringField('Country',
                        validators=[DataRequired(), Length(min=2, max=25)])
    cellphone = TelField('Cellphone',
                         validators=[DataRequired(), Length(min=9, max=30)])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

    def validate_cellphone(self, cellphone):
        if not cellphone.data.isdigit():
            raise ValidationError('Cellphone needs to be in digit form!')
        else:
            if int(cellphone.data) != current_user.cellphone:
                user = User.query.filter_by(cellphone=cellphone.data).first()
                if user:
                    raise ValidationError('That cellphone is taken. Please choose a different one.')


class VerificationForm(FlaskForm):
    number = StringField('Number', validators=[DataRequired(), Length(min=6, max=20)])
    name = StringField('Name', validators=[DataRequired()])
    expires = StringField('Expires', validators=[DataRequired()])
    ccv = TelField('CCV', validators=[DataRequired(), Length(min=3, max=3)])
    submit = SubmitField('Activate')

    def validate_number(self, number):
        if number.data != "4242424242424242" and number.data != "4242 4242 4242 4242":
            raise ValidationError('Card number is invalid')

    def validate_name(self, name):
        if name.data != current_user.name:
            raise ValidationError('Name is invalid')

    def validate_expires(self, expires):
        if expires.data != "02/23":
            raise ValidationError('Expire Date is invalid')

    def validate_ccv(self, ccv):
        if ccv.data != "123":
            raise ValidationError('CCV is invalid')
