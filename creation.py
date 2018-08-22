import mysql.connector
from mysql.connector import errorcode
from database import Database
from script import Script


class Creation(Database):
    def create_database(self):
        relativePath = r"queries\createDatabase.sql"
        scrt = Script()
        cnx = mysql.connector.connect()
        sqlCommands = scrt.read_script(scrt.join_path(relativePath))

        try:
            cnx = mysql.connector.connect(user=self.USER, password=self.PASSWORD,
                                          host=self.HOST)
            cursor = cnx.cursor()

            for command in sqlCommands:
                cursor.execute(command)
        except Exception as e:
            print(e)
        finally:
            cnx.close()

        print("DATABASE CREATED!")

    def create_proc_user(self):
        relativePath = r"queries\insertUser.sql"
        scrt = Script()
        cnx = self.get_connector()
        sqlCommands = scrt.read_script(scrt.join_path(relativePath))

        try:
            cursor = cnx.cursor()

            for command in sqlCommands:
                cursor.execute(command)
        except Exception as e:
            print(e)
        finally:
            cnx.close()

        print("PROCEDURE CREATED!")

    def create_proc_user_data(self):
        relativePath = r"queries\insertData.sql"
        scrt = Script()
        cnx = self.get_connector()
        sqlCommands = scrt.read_script(scrt.join_path(relativePath))

        try:
            cursor = cnx.cursor()

            for command in sqlCommands:
                cursor.execute(command)
        except Exception as e:
            print(e)
        finally:
            cnx.close()

        print("PROCEDURE CREATED!")

    def create_proc_update_data(self):
        relativePath = r"queries\updateDateModi.sql"
        scrt = Script()
        cnx = self.get_connector()
        sqlCommands = scrt.read_script(scrt.join_path(relativePath))

        try:
            cursor = cnx.cursor()

            for command in sqlCommands:
                cursor.execute(command)
        except Exception as e:
            print(e)
        finally:
            cnx.close()

        print("PROCEDURE CREATED!")

    def create_proc_get_files(self):
        relativePath = r"queries\getFiles.sql"
        scrt = Script()
        cnx = self.get_connector()
        sqlCommands = scrt.read_script(scrt.join_path(relativePath))

        try:
            cursor = cnx.cursor()

            for command in sqlCommands:
                cursor.execute(command)
        except Exception as e:
            print(e)
        finally:
            cnx.close()

        print("PROCEDURE CREATED!")

    def create_proc_get_users(self):
        relativePath = r"queries\getUsers.sql"
        srct = Script()
        cnx = self.get_connector()
        sqlCommands = srct.read_script(srct.join_path(relativePath))

        try:
            cursor = cnx.cursor()

            for command in sqlCommands:
                cursor.execute(command)
        except Exception as e:
            print(e)
        finally:
            cnx.close()
        print("PROCEDURE CREATED!")
