import pymysql



def create_database(database):
    drop_accounts_table = 'DROP TABLE IF EXISTS accounts;'
    create_accounts_table = """CREATE TABLE IF NOT EXISTS accounts 
                                        (id INTEGER PRIMARY KEY, 
                                        account_number INTEGER NOT NULL, 
                                        account_balance varchar(250) NOT NULL, 
                                        users_id INTEGER NOT NULL, 
                                        FOREIGN KEY(users_id) REFERENCES users(id))"""
    drop_users_table = 'DROP TABLE IF EXISTS users;'
    create_users_table = """CREATE TABLE IF NOT EXISTS users 
                                        (id INTEGER PRIMARY KEY, 
                                        name varchar(250) NOT NULL, 
                                        surname varchar(250) NOT NULL,
                                        pesel BIGINT NOT NULL, 
                                        address varchar(250) NOT NULL,
                                        login_id INTEGER OT NULL,
                                        account_id INTEGER NOT NULL,
                                        FOREIGN KEY (login_id) REFERENCES logins(id),
                                        FOREIGN KEY (account_id) REFERENCES accounts(id)    )"""
    drop_logins_table = 'DROP TABLE IF EXISTS logins;'
    create_logins_table = """CREATE TABLE IF NOT EXISTS logins 
                                        (id INTEGER PRIMARY KEY, 
                                        login varchar(250) NOT NULL, 
                                        password varchar(250) NOT NULL, 
                                        users_id INTEGER NOT NULL, 
                                        accounts_id INTEGER NOT NULL, 
                                        FOREIGN KEY (users_id) REFERENCES users(id),
                                        FOREIGN KEY (accounts_id) REFERENCES accounts(id))"""

    accounts_data = (
        (None, '162472', '36589.99', '1'),
        (None, '244685', '12260.87', '2'),
        (None, '805054', '87329.63', '3'),
    )

    users_data = (
        (None, 'Tomasz', 'Nowak', '53515564843', 'Poznań 60-320 Bukowska 1/2', '1', '1'),
        (None, 'Alfred', 'Szymczak', '74300625537', 'Gorzów Wlkp. 66-400 Stilonowa 13/8', '2', '2'),
        (None, 'Jan', 'Kowalski', '38300020761', 'Warszawa 01-020 Marszałowska 121/12', '3', '3')
    )

    logins_data = (
        (None, '1234', 'zxcv', '1', '1'),
        (None, '2345', 'asdf', '2', '2'),
        (None, '3456', 'qwer', '3', '3')
    )

    # utworzenie połączenia z bazą
    db = pymysql.connect("localhost", "root", "Vifon", database)
    cur = db.cursor()

    # utworzenie tabel
    cur.execute(drop_accounts_table)
    cur.execute(create_accounts_table)
    cur.execute(drop_users_table)
    cur.execute(create_users_table)
    cur.execute(drop_logins_table)
    cur.execute(create_logins_table)
    # wypełnienie tabel danymi
    cur.executemany('INSERT INTO accounts VALUES(?,?,?,?);', accounts_data)
    cur.executemany('INSERT INTO users VALUES(?,?,?,?,?,?,?);', users_data)
    cur.executemany('INSERT INTO logins VALUES(?,?,?,?,?);', logins_data)
    # zatwierdzamy zmiany w bazie
    conn.commit()


create_database('vifon')