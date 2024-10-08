from flask import Flask, request, render_template, flash, redirect, url_for
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def index():
    return redirect(url_for('contact'))

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form = form)
        else:
            return render_template('success.html')
    if request.method == 'GET':
        return render_template('contact.html', form = form)
    
if __name__ == '__main__':
    app.run(debug=True)