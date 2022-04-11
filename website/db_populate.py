import sqlite3

def populate_database():
    db_locale = 'autoz_database.db'

    conn = sqlite3.connect(db_locale)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO user (employee_id, role, firstname, lastname, phone, email, password) VALUES
    (234567, 'security-analyst', 'Bob', 'Preston', 897152236, 'bobpreston@email.com', 'secret123'),
    (789012, 'security-analyst', 'Susan', 'Sage', 775321654, 'susansage@email.com', 'secret456'),
    (345678, 'security-analyst', 'James', 'Button', 741852963, 'jamebutton@email.com', 'secret789'),
    (901234, 'security-analyst', 'Emilly', 'Carlton', 147258369, 'emillycarlton@email.com', 'secret012'),
    (567890, 'security-analyst', 'Dave', 'Chapelle', 748159263, 'davechapelle@email.com', 'secret345'),
    (987654, 'security-analyst', 'Son', 'Goku', 326159487, 'songoku@email.com', 'secret678'),
    (654987, 'supervisor', 'Yuji', 'Itadori', 791346258, 'yujiitadori@email.com', 'supersecret123'),
    (321987, 'it-director', 'Sasuke', 'Uchiha', 175369147, 'sasukeuchiha@email.com', 'supersecret456'),
    (987321, 'cisso', 'John', 'Wick', 852741901, 'johnwick@email.com', 'supersecret789')
    """)

    cursor.execute("""
    INSERT INTO ato_form (type, status, owner, os_build, version, serial_num, mac_num, creator, date, eol, descr) VALUES
    ('Hardware','Approved', 3, '3.02.1', '2.3', 123456789456123, 'mac987654321', 'Portswigger', "2020, 5, 4", "2025, 5, 4", "This is awesome"),
    ('Software','Pending', 3, '13.1', '1.2.3', 654987321456789, 'mac321654785', 'Windows', "2021, 2, 13", "2023, 5, 11", "I prefer Linux systems for hacking"),
    ('Hardware','Pending', 4, '2.01', '12.7', 987654789654789, 'mac123123123', 'Linux', "2019, 5, 4", "2025, 5, 4", "Winner Winner!! Chicken Dinner!!"),
    ('Hardware','Approved', 5, '3.02.1', '2.3', 951951847847847, 'mac456456789', 'WireShark', "2020, 10, 13", "2025, 5, 4", "I look at packets over the network through any connection"),
    ('Software','Approved', 3, '3.02.1', '2.3', 123456789456123, 'mac741741852', 'FireEye', "2021, 12, 23", "2025, 5, 4", "My eye is on fire because of the Mangekyo Sharigan"),
    ('Software','Pending', 6, '3.02.1', '2.3', 623623951951951, 'mac852963741', 'DragonBallZ', "2021, 10, 10", "2025, 5, 4", "I have finally mastered AUTONOMOUS ULTRA INSTINCT"),
    ('Hardware','Approved', 6, '3.02.1', '2.3', 487847847159159, 'mac369369369', 'HunterxHunter', "2022, 8, 30", "2025, 5, 4", "You will bring back Kite . . ."),
    ('Hardware','Denied', 1, '3.02.1', '2.3', 621954874951236, 'mac951847847', 'LeafVillage', "2022, 3, 4", "2025, 5, 4", "As the 5th Hokage, I approve this message"),
    ('Software','Approved', 1, '3.02.1', '2.3', 931793179317741, 'mac179317931', 'UchihaClan', "2019, 5, 21", "2025, 5, 4", "I miss my clan"),
    ('Hardware','Denied', 2, '3.02.1', '2.3', 741654789321456, 'mac951478521', 'WaterHavean', "2021, 6, 4", "2025, 5, 4", "Blah blah blah blah . . . Elden Ring")
    """)

    cursor.execute(
        """INSERT INTO login (username, password) 
        VALUES('walt@autozone.com', 'password1'),
        ('bob', 'password2')"""
    )

    conn.commit()
    conn.close()