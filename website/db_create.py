import sqlite3

def create_database():
    db_locale = 'autoz_database.db'

    conn = sqlite3.connect(db_locale)
    cursor = conn.cursor()

    cursor.execute("""
    DROP TABLE IF EXISTS user;
    """)

    cursor.execute("""
    DROP TABLE IF EXISTS ato_form;
    """)

    cursor.execute("""
    CREATE TABLE user 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    phone INTEGER NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
    )""")

    cursor.execute("""
    CREATE TABLE ato_form 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner INTEGER NOT NULL,
    type TEXT NOT NULL,
    os_build TEXT,
    version INTEGER,
    serial_num INTEGER,
    mac_num TEXT,
    creator TEXT,
    date DATE,
    eol DATE,
    descr TEXT,
    status TEXT,
    FOREIGN KEY (owner) REFERENCES user (id)
    )
    """)

    conn.commit()
    conn.close()