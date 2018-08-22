import mysql.connector
from mysql.connector import errorcode
from script import Script
from datetime import datetime


class Database:

    USER = "root"
    PASSWORD = "ADDPW"
    DATABASE = "challenge"
    HOST = "127.0.0.1"

    def get_connector(self):
        cnx = cnx = mysql.connector.connect()

        try:
            cnx = mysql.connector.connect(user=self.USER, password=self.PASSWORD,
                                          host=self.HOST, database=self.DATABASE)
        except Exception as e:
            print(e)

        return cnx

    def exist_database(self):
        cnx = self.get_connector()

        try:
            cursor = cnx.cursor()

            sql = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA " + \
                  "WHERE SCHEMA_NAME = '" + self.DATABASE + "'"

            r = cursor.execute(sql)

            r = cursor.fetchall()

            if r != None:
                return True

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                return False
        finally:
            cnx.close()
