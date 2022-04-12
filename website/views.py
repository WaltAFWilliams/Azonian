from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_login import login_required, current_user
import sqlite3


views = Blueprint('views', __name__)


@views.route('/index')
@login_required
def index():
    card_data = query_ato_count()
    ato_data = query_ato_details()
    green = "Approved"
    orange = "Pending"
    red = "Denied"
    return render_template('index.html', user=current_user, card_data=card_data, ato_data=ato_data, green=green, orange=orange, red=red)


@views.route('/new_form', methods=['GET', 'POST'])
@login_required
def new_form():
    # If they're trying to save the form to the database
    if request.method == 'GET':
        return render_template('new_form.html')
    else:
        flash('ATO added!', 'success')
        ato_info = (
            request.form['firstName'],
            request.form['lastName'],
            request.form['emp_id'],
            1,
            'Hardware',
            request.form['os_build'],
            request.form['version'],
            request.form['serial_num'],
            request.form['mac_num'],
            request.form['creator'],
            request.form['date'],
            request.form['eol'],
            request.form['description'],
            'Pending'
        )
        
        insert_info(ato_info)
        return redirect(url_for('views.index'), user=current_user)

def insert_info(ato_info):
    db_locale = 'autoz_database.db'

    conn = sqlite3.connect(db_locale)
    cursor = conn.cursor()

    sql_execute = 'INSERT INTO ato_form (owner, type, os_build, version, serial_num, mac_num, creator, date, eol, descr, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    
    cursor.execute(sql_execute, ato_info)

    conn.commit()
    conn.close()  

def query_ato_count():
    db_locale = 'autoz_database.db'

    conn = sqlite3.connect(db_locale)
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT type, COUNT(type) 
        FROM ato_form
        GROUP BY type;
    """)

    ato_count = cursor.fetchall()

    return ato_count

def query_ato_details():
    db_locale = 'autoz_database.db'

    conn = sqlite3.connect(db_locale)
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT employee_id, first_Name, last_Name, ato_form.status
    FROM user
    INNER JOIN ato_form on ato_form.owner = user.id;
    """)

    ato_data = cursor.fetchall()

    return ato_data