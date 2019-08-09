### Used only to create tables in database and fill it with data, database have to be created separatedly
### Foreign keys need to be added manualy


import pymysql


def create_database(database):
    create_accounts_table = """CREATE TABLE IF NOT EXISTS accounts 
                                        (id INT NOT NULL AUTO_INCREMENT, 
                                        account_number INT NOT NULL, 
                                        account_balance VARCHAR(250) NOT NULL,
                                        PRIMARY KEY(id))"""

    create_users_table = """CREATE TABLE IF NOT EXISTS users 
                                        (id INT NOT NULL AUTO_INCREMENT, 
                                        name VARCHAR(250) NOT NULL, 
                                        surname VARCHAR(250) NOT NULL,
                                        pesel BIGINT NOT NULL, 
                                        address VARCHAR(250) NOT NULL,
                                        login_id INT NOT NULL,
                                        account_id INT NOT NULL,
                                        PRIMARY KEY(id))"""

    create_logins_table = """CREATE TABLE IF NOT EXISTS logins 
                                        (id INT NOT NULL AUTO_INCREMENT, 
                                        login VARCHAR(250) NOT NULL, 
                                        password varchar(250) NOT NULL,
                                        PRIMARY KEY(id))"""

    accounts_data = (
        (None, '162472', '36589.99'),
        (None, '244685', '12260.87'),
        (None, '805054', '87329.63'),
    )

    users_data = (
        (None, 'Tomasz', 'Nowak', '53515564843', 'Poznan 60 320 Bukowska 1 2', 1, 1),
        (None, 'Alfred', 'Szymczak', '74300625537', 'Gorzow Wlkp 66 400 Stilonowa 13 8', 2, 2),
        (None, 'Jan', 'Kowalski', '38300020761', 'Warszawa 01 020 Marszalkowska 121 12', 3, 3)
    )

    logins_data = (
        (None, '1234', 'zxcv'),
        (None, '2345', 'asdf'),
        (None, '3456', 'qwer')
    )

    # utworzenie połączenia z bazą
    db = pymysql.connect("localhost", "root", "Vifon", database)
    cur = db.cursor()

    # utworzenie tabel
    cur.execute(create_accounts_table)
    cur.execute(create_users_table)
    cur.execute(create_logins_table)
    # wypełnienie tabel danymi
    cur.executemany('INSERT INTO accounts VALUES(%s, %s, %s)', accounts_data)
    cur.executemany('INSERT INTO users VALUES(%s, %s, %s, %s, %s, %s, %s)', users_data)
    cur.executemany('INSERT INTO logins VALUES(%s, %s, %s)', logins_data)
    # zatwierdzamy zmiany w bazie
    db.commit()
    cur.close()
    db.close()
