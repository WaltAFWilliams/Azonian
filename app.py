from distutils.log import debug
from json.tool import main
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_form', methods=['GET', 'POST'])
def new_form():
    # If they're trying to save the form to the database
    if request.method == 'POST':
        return redirect(url_for('index'))

    # If they're trying to create a new ATO form
    return render_template('new_form.html')

if __name__ == '__main__':
    app.run(debug=True)