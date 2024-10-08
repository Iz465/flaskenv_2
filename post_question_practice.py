from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/finish', methods = ['POST'])
def finish():
    if request.method == 'POST':
        name = request.form['user']
        return render_template('form_finish.html', names = name)

if __name__ == '__main__':
    app.run(debug=True)