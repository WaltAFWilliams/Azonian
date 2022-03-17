from flask import Blueprint, render_template, url_for, request, redirect
from json.tool import main


views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/new_form', methods=['GET', 'POST'])
def new_form():
    # If they're trying to save the form to the database
    if request.method == 'POST':
        return redirect(url_for('index'))

    # If they're trying to create a new ATO form
    return render_template('new_form.html')