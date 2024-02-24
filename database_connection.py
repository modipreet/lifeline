# database_connection.py
import mysql.connector

class DatabaseConnection:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, data=None):
        if data:
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
