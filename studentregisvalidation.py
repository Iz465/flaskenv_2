from flask import Flask, render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Email, EqualTo
import sqlite3 as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class StudentRegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=10, max=99)])
    address = TextAreaField('Address', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    confirm_email = StringField('Confirm Email', validators=[DataRequired(), Email(), EqualTo('email')])
    password = StringField('Password', validators=[DataRequired(), Length(min = 5, max= 10) ])
    confirm_password = StringField('Password', validators=[DataRequired(), Length(min = 5, max= 10), EqualTo('password') ])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def registration():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        flash(f'Student {form.name.data} registered successfully!', 'success')
        Name = request.form['name']
        Age = request.form['age']
        Address = request.form['address']
        Phone = request.form['phone']
        Email = request.form['email']
        Password = request.form['password']
        if not Name or Age or Address or Phone or Email:
            with sql.connect('enrollment.db') as con:
                cur = con.cursor()
                cur.execute('Insert into Student2(Name, Age, Address, Phone, Email, Password) values(?,?,?,?,?,?)',
                            (Name,Age,Address,Phone,Email, Password))
                con.commit()
        return render_template('studentregistered.html')
    return render_template('registrationvalidation.html', title='Student Registration', form=form)

@app.route('/list')
def list():
    con = sql.connect('enrollment.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from Student2")
    rows = cur.fetchall()
    return render_template('list_2.html', rows = rows)




if __name__ == '__main__':
    app.run(debug=True)
