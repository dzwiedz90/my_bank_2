import pymysql
from typing import List


class DatabaseActions:
    def __init__(self):
        self._database = 'vifon'

    def get_login_and_password(self, user_login: str) -> List[tuple]:
        db = pymysql.connect("localhost", "root", "Vifon", self._database)
        cur = db.cursor()
        try:
            cur.execute("SELECT login, password FROM logins WHERE login = '" + user_login + "'")
            data = cur.fetchone()
            db.commit()
            cur.close()
            db.close()
            return data
        except TypeError:
            print('Wrong login or password!')

    def get_account_data(self, user_login: str) -> str:
        db = pymysql.connect("localhost", "root", "Vifon", self._database)
        cur = db.cursor()
        cur.execute("select l.login, u.name, u.surname, a.account_number, a.account_balance "
                    "from users u join accounts a on u.account_id = a.id join logins l on u.login_id = l.id "
                    "where l.login = '" + user_login + "'")
        data = cur.fetchone()
        db.commit()
        cur.close()
        db.close()
        return f'Login: {data[0]}\n{data[1]} {data[2]}\nNumer konta: {data[3]}\nStan konta: {round(float(data[4]), 2)}'

    def transfer_money(self, user_login: str, amount_to_transfer: str) -> None:
        db = pymysql.connect("localhost", "root", "Vifon", self._database)
        cur = db.cursor()
        cur.execute("select id from logins where login = '" + user_login + "'")
        login_id = cur.fetchone()
        cur.execute("select account_balance from accounts where id = '" + str(login_id[0]) + "'")
        balance = cur.fetchone()
        amount = float(balance[0]) - float(amount_to_transfer)
        cur.execute("update accounts set account_balance = '" + str(amount) + "' where id= '" + str(login_id[0]) + "'")
        db.commit()
        cur.close()
        db.close()
