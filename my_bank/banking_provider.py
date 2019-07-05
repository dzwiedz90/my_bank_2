import abc
import sqlite3
from typing import List


class AbstractBankingProvider(abc.ABC):

    @abc.abstractmethod
    def log_in(self, user_id: int, user_pass: str) -> None:
        raise NotImplemented

    @abc.abstractmethod
    def check_if_logged(self, user_id: int) -> bool:
        raise NotImplemented

    @abc.abstractmethod
    def get_account_data(self, user_id: int) -> List:
        raise NotImplemented

    @abc.abstractmethod
    def transfer(self, user_id: int, amount_to_transfer: float, target_account: int) -> None:
        raise NotImplemented

    @abc.abstractmethod
    def log_out(self, user_id: int) -> None:
        raise NotImplemented


class SQLiteBankingProvider(AbstractBankingProvider):
    def __init__(self, database):
        self._logged_in = False
        self._database = database

        self._drop_accounts_table = 'DROP TABLE IF EXISTS accounts;'
        self._create_accounts_table = """CREATE TABLE IF NOT EXISTS accounts 
                                    (id INTEGER PRIMARY KEY ASC, 
                                    account_number INTEGER NOT NULL, 
                                    account_balance varchar(250) NOT NULL, 
                                    users_id INTEGER NOT NULL, 
                                    FOREIGN KEY(users_id) REFERENCES users(id))"""
        self._drop_users_table = 'DROP TABLE IF EXISTS users;'
        self._create_users_table = """CREATE TABLE IF NOT EXISTS users 
                                    (id INTEGER PRIMARY KEY ASC, 
                                    name varchar(250) NOT NULL, 
                                    surname varchar(250) NOT NULL,
                                    pesel BIGINT NOT NULL, 
                                    address varchar(250) NOT NULL,
                                    login_id INTEGER OT NULL,
                                    account_id INTEGER NOT NULL,
                                    FOREIGN KEY (login_id) REFERENCES logins(id),
                                    FOREIGN KEY (account_id) REFERENCES accounts(id)    )"""
        self._drop_logins_table = 'DROP TABLE IF EXISTS logins;'
        self._create_logins_table = """CREATE TABLE IF NOT EXISTS logins 
                                    (id INTEGER PRIMARY KEY ASC, 
                                    login varchar(250) NOT NULL, 
                                    password varchar(250) NOT NULL, 
                                    users_id INTEGER NOT NULL, 
                                    accounts_id INTEGER NOT NULL, 
                                    FOREIGN KEY (users_id) REFERENCES users(id),
                                    FOREIGN KEY (accounts_id) REFERENCES accounts(id))"""

        conn = self.connect_db(self._database)
        if conn is not None:
            self.create_table(conn, self._drop_users_table)
            self.create_table(conn, self._create_users_table)
            self.create_table(conn, self._drop_accounts_table)
            self.create_table(conn, self._create_accounts_table)
            self.create_table(conn, self._drop_logins_table)
            self.create_table(conn, self._create_logins_table)
            conn.commit()
        else:
            print("Error! cannot create the database connection.")

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
                        (None, '1234', '1234', '1', '1'),
                        (None, '2345', '2345', '2', '2'),
                        (None, '3456', '3456', '3', '3')
                      )

        self.insert_data_into_tables(conn, accounts_data, users_data, logins_data)

    def connect_db(self, database):
        try:
            conn = sqlite3.connect(database)
            return conn
        except sqlite3.Error as e:
            print(e)
        return None

    def create_table(self, conn, create_table_sql) -> None:
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)

    def insert_data_into_tables(self, conn, accounts_data: tuple, users_data: tuple, logins_data: tuple) -> None:
        cur = conn.cursor()
        cur.executemany('INSERT INTO accounts VALUES(?,?,?,?)', accounts_data)
        cur.executemany('INSERT INTO users VALUES(?,?,?,?,?,?,?)', users_data)
        cur.executemany('INSERT INTO logins VALUES(?,?,?,?,?)', logins_data)

    def log_in(self, user_id: int, user_pass: str) -> None:
        pass

    def check_if_logged(self, user_id: int) -> bool:
        return self._logged_in

    def get_account_data(self, user_id: int) -> List:
        pass

    def transfer(self, user_id: int, amount_to_transfer: float, target_account: int) -> None:
        pass

    def log_out(self, user_id: int) -> None:
        pass


x = SQLiteBankingProvider('resources/my_bank.db')