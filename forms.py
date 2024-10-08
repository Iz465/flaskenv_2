from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError

class ContactForm(FlaskForm):
    name = TextField("Name of Student",[validators.Required("Please enter your name.")])
    gender = RadioField("Gender", choices = [('M', 'Male'), ('F', 'Female'),('O', 'Other')])
    address = TextAreaField("Address")
    email = TextField("Email",[validators.Required("Please enter in your email address"), validators.Email("Please enter your email address in the correct format")])
    age = IntegerField("Age")
    language = SelectField("Language", choices = [('cpp', 'c++'), ('py', 'python')])
    submit = SubmitField("Send")