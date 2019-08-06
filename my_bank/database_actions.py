import mysql.connector
from typing import List


class CreateDatabase:
    def __init__(self, database):
        self._database = database

        # self._drop_accounts_table = 'DROP TABLE IF EXISTS accounts;'
        # self._create_accounts_table = """CREATE TABLE IF NOT EXISTS accounts
        #                                     (id INTEGER PRIMARY KEY ASC,
        #                                     account_number INTEGER NOT NULL,
        #                                     account_balance varchar(250) NOT NULL,
        #                                     users_id INTEGER NOT NULL,
        #                                     FOREIGN KEY(users_id) REFERENCES users(id))"""
        # self._drop_users_table = 'DROP TABLE IF EXISTS users;'
        # self._create_users_table = """CREATE TABLE IF NOT EXISTS users
        #                                     (id INTEGER PRIMARY KEY ASC,
        #                                     name varchar(250) NOT NULL,
        #                                     surname varchar(250) NOT NULL,
        #                                     pesel BIGINT NOT NULL,
        #                                     address varchar(250) NOT NULL,
        #                                     login_id INTEGER OT NULL,
        #                                     account_id INTEGER NOT NULL,
        #                                     FOREIGN KEY (login_id) REFERENCES logins(id),
        #                                     FOREIGN KEY (account_id) REFERENCES accounts(id)    )"""
        # self._drop_logins_table = 'DROP TABLE IF EXISTS logins;'
        # self._create_logins_table = """CREATE TABLE IF NOT EXISTS logins
        #                                     (id INTEGER PRIMARY KEY ASC,
        #                                     login varchar(250) NOT NULL,
        #                                     password varchar(250) NOT NULL,
        #                                     users_id INTEGER NOT NULL,
        #                                     accounts_id INTEGER NOT NULL,
        #                                     FOREIGN KEY (users_id) REFERENCES users(id),
        #                                     FOREIGN KEY (accounts_id) REFERENCES accounts(id))"""
        #
        # accounts_data = (
        #     (None, '162472', '36589.99', '1'),
        #     (None, '244685', '12260.87', '2'),
        #     (None, '805054', '87329.63', '3'),
        # )
        #
        # users_data = (
        #     (None, 'Tomasz', 'Nowak', '53515564843', 'Poznań 60-320 Bukowska 1/2', '1', '1'),
        #     (None, 'Alfred', 'Szymczak', '74300625537', 'Gorzów Wlkp. 66-400 Stilonowa 13/8', '2', '2'),
        #     (None, 'Jan', 'Kowalski', '38300020761', 'Warszawa 01-020 Marszałowska 121/12', '3', '3')
        # )
        #
        # logins_data = (
        #     (None, '1234', 'zxcv', '1', '1'),
        #     (None, '2345', 'asdf', '2', '2'),
        #     (None, '3456', 'qwer', '3', '3')
        # )
        #
        # try:
        #     # utworzenie połączenia z bazą
        #     conn = sqlite3.connect(self._database)
        #     cur = conn.cursor()
        #     # utworzenie tabel
        #     cur.execute(self._drop_accounts_table)
        #     cur.execute(self._create_accounts_table)
        #     cur.execute(self._drop_users_table)
        #     cur.execute(self._create_users_table)
        #     cur.execute(self._drop_logins_table)
        #     cur.execute(self._create_logins_table)
        #     # wypełnienie tabel danymi
        #     cur.executemany('INSERT INTO accounts VALUES(?,?,?,?);', accounts_data)
        #     cur.executemany('INSERT INTO users VALUES(?,?,?,?,?,?,?);', users_data)
        #     cur.executemany('INSERT INTO logins VALUES(?,?,?,?,?);', logins_data)
        #     # zatwierdzamy zmiany w bazie
        #     conn.commit()
        # except sqlite3.Error as e:
        #     print(e)

    def get_login_and_password(self, user_login: str) -> List[tuple]:
        conn = sqlite3.connect(self._database)
        cur = conn.cursor()
        cur.execute("SELECT login, password FROM logins WHERE login=?;", [(user_login)])
        data = cur.fetchall()
        return data

    def get_account_data(self, user_id: str) -> List[tuple]:
        conn = sqlite3.connect(self._database)
        cur = conn.cursor()
        # (
        #     "SELECT orders.id, clients.name, clients.surname, clients.city, clients.post_code, "
        #     "clients.street_home_number, products.product_name, products.price from orders INNER JOIN clients "
        #     "ON orders.client_id = clients.id INNER JOIN products ON orders.product_id = products.id;")
        cur.execute("""
                        SELECT users.name, users.surname, users.pesel, users.address, accounts.account_number,
                        accounts.account_balance, logins.login
                        FROM users, accounts, logins WHERE logins.login = ?
                        INNER JOIN accounts ON users.account_id = accounts.id
                        INNER JOIN logins ON users.login_id = logins.id
                    """, [(user_id)])
        data = cur.fetchall()
        return data