import sqlite3

def populate_database():
    db_locale = 'autoz_database.db'

    conn = sqlite3.connect(db_locale)
    cursor = conn.cursor()

    # password = ['secret123', 'secret456', 'secret789', 'secret012', 'secret345', 'secret678', 'supersecret123', 'supersecret456', 'supersecret789']

    cursor.execute("""
    INSERT INTO user (employee_id, role, first_Name, last_Name, phone, email, password) VALUES
    (234567, 'security-analyst', 'Bob', 'Preston', 8971522360, 'bobpreston@email.com', 'sha256$7F5F5EBYgUo0S0iD$defebefdb9dde2770b707a902ee6bbe6cc2531388c55290743477abbdb1e287e'),
    (789012, 'security-analyst', 'Susan', 'Sage', 7753216540, 'susansage@email.com', 'sha256$NqCBqqDKrn861nJf$b78283e8f2f9d2da11c6820430474c92e64f8e21bd6d314e23c5018293ad04ef'),
    (345678, 'security-analyst', 'James', 'Button', 7418529630, 'jamebutton@email.com', 'sha256$bQIFw5P2wKjEq3aO$d0fac9cbefb8c16304ca320cfc669eefba045f4bb9b3d6364de836e22107a52c'),
    (901234, 'security-analyst', 'Emilly', 'Carlton', 1472583690, 'emillycarlton@email.com', 'sha256$a7AuS2nIBZnxZUDg$ebba7a673721052689dddd1fb66df0fc52c6949673883f423c5f4124bea8241e'),
    (567890, 'security-analyst', 'Dave', 'Chapelle', 7481592630, 'davechapelle@email.com', 'sha256$zQWg7m86cWWD4T3j$1413b787300b2df253cd8e3e7c53b90536273e02cde24fa83465f57d6aecdea3'),
    (987654, 'security-analyst', 'Son', 'Goku', 3261594870, 'songoku@email.com', 'sha256$aXcevgF0OM30nGKj$bb8bd2533fc35240e36d1afebee91fcf94509276985ce3c5f678f9217eef6007'),
    (654987, 'supervisor', 'Yuji', 'Itadori', 7913462580, 'yujiitadori@email.com', 'sha256$6PT4N084VSZkn6EH$d63535b1fa18cb3111678b4a0c2944bbeacdcf2f6d886d1ffd1677b71c1d4fc6'),
    (321987, 'it-director', 'Sasuke', 'Uchiha', 1753691470, 'sasukeuchiha@email.com', 'sha256$VcJ4VjU4ehpZA8p4$616d4bf1474f88a576e6a091748c2c881645f2ea55756d0757a4993e40d10733'),
    (987321, 'cisso', 'John', 'Wick', 8527419010, 'johnwick@email.com', 'sha256$7dorNVNM71v1e0iW$060526e1c9a1787c82b52cdb3be6ec35cea56281dbf4d0f1748b7376852266cc')
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

    conn.commit()
    conn.close()

    
    