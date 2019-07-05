import sqlite3


class DatabaseActions:
    def __init__(self, database):
        self._database = database

    def create_db(self, database):
        try:
            conn = sqlite3.connect(database)
            return conn
        except sqlite3.Error as e:
            print(e)

        return None

    def create_table(self, conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)


x = DatabaseActions('resources/database.db')
