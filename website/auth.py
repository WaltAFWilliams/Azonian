import uuid
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.index'))
            else:
                flash('Email or password was incorrect. Please try again.1', 'error')
        else:
            flash('Email or password was incorrect. Please try again.2', 'error')

    return render_template('login_page.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        role = request.form['role']
        email = request.form['email']
        phone = request.form['phone']
        password1 = request.form['password1']
        password2 = request.form['password2']

        user = User.query.filter_by(email=email).first()
        # Check if information is valid
        if user:
            flash('Email or password was incorrect. Please try again.', 'error')
        elif len(firstName) < 1:
            flash('First name is required', 'error')
        elif len(lastName) < 1:
            flash('Last name is required', 'error')
        elif len(role) < 1:
            flash('Role is required', 'error')
        elif len(email) < 4:
            flash('Email must be more than 4 characters', 'error')
        elif len(phone) < 10:
            flash('Phone number is required', 'error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters', 'error')
        elif password1 != password2:
            flash('Passwords do not match', 'error')
        else:
            emp_id = uuid.uuid3(uuid.NAMESPACE_DNS, firstName + lastName)
            new_user = User(employee_id=emp_id.time_mid, role=role, first_name=firstName, last_name=lastName, phone=phone, email=email, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User successfully created', 'success')
            
            return redirect(url_for('views.index'))

    return render_template('new_account_page.html', user=current_user)