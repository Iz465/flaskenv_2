from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('newstudent.html')

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    if request.method == 'POST':
        try:
            FirstName = request.form['FirstName']
            LastName = request.form['LastName']
            Address = request.form['Address']
            City = request.form['City']
            if not FirstName or LastName or Address or City:
                with sql.connect("enrollment.db") as con:
                    cur = con.cursor()
                    cur.execute("Insert into Student1(FirstName, LastName, Address, City) values(?,?,?,?)", 
                                (FirstName, LastName, Address, City))
                    con.commit()
                    msg = 'Record successfully added'
            else:
                msg = 'error in insert operation'
        
        except:
            msg = 'error in insert operation'
            con.rollback()
        finally: 
            return render_template('addresult.html', msg = msg)


@app.route('/list')
def list():
    con = sql.connect('enrollment.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from Student1")
    rows = cur.fetchall()
    return render_template('list.html', rows = rows)


if __name__ == '__main__':
    app.run(debug=True)