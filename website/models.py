import sqlite3

def insert_user(username, password):
    db_locale = 'autoz_database.db'

    conn = sqlite3.connect(db_locale)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO user (username, password) VALUES (?,?)", (username, password))
    conn.commit()
    conn.close()

def retrieve_users():
    db_locale = 'autoz_database.db'

    conn = sqlite3.connect(db_locale)
    cursor = conn.cursor()

    cursor.execute("SELECT username, password from login")
    users = cursor.fetchall()
    conn.close()

