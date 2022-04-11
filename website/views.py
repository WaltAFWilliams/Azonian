from crypt import methods
from multiprocessing.sharedctypes import Value
from flask import Blueprint, render_template, url_for, request, redirect, flash
import sqlite3
from json.tool import main


views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
def login_page():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = sqlite3.connect('autoz_database.db')
        cursor = conn.cursor()        
        query = cursor.execute('SELECT (username, password) from login where username=(?) and password=(?)', [email, password])
        valid_user = query.fetchone()
        if valid_user is not None:
            return redirect(url_for('index.html'))
        else: 
            raise ValueError(' This email is not registered, please create a new account.')
            return render_template('login_page.html')
    else:
        return render_template('login_page.html')

@views.route('/new_account', methods=['GET', 'POST'])
def new_account_page():
    if request.method=='POST': # If the user is trying to save their information into the database
        username = request.form['email']
        password = request.form['password']
        insert_user(username, password)
        return redirect(url_for('index.html'))
    else:
        return render_template('new_account_page.html')


@views.route('/index')
def index():
    card_data = query_ato_count()
    ato_data = query_ato_details()
    green = "Approved"
    orange = "Pending"
    red = "Denied"
    return render_template('index.html', card_data=card_data, ato_data=ato_data, green=green, orange=orange, red=red)


@views.route('/add', methods=['GET', 'POST'])
def new_form():
    # If they're trying to save the form to the database
    if request.method == 'GET':
        return render_template('new_form.html')
    else:
        # flash('ATO added!', category='success')
        owner_info = (
            request.form['firstName'],
            request.form['lastName'],
            request.form['emp_id']
        )

        ato_info = (
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
        return redirect(url_for('views.index'))

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
    SELECT employee_id, firstname, lastname, ato_form.status
    FROM user
    INNER JOIN ato_form on ato_form.owner = user.id;
    """)

    ato_data = cursor.fetchall()

    return ato_data