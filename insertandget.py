import mysql.connector
from mysql.connector import errorcode
from database import Database
from script import Script
from datetime import datetime


class InsertAndGet(Database):
    def insert_user(self, args):
        cnx = self.get_connector()
        try:
            cursor = cnx.cursor()

            cursor.callproc('sp_InsertUser', args)
            cnx.commit()
        except Exception as e:
            print(e)
        finally:
            cnx.close()

    def orderdata(self, a):
        aux = []

        aux.append(a['name'])

        try:
            aux.append(a['fullFileExtension'])
        except:
            aux.append("NN")

        aux.append(a['owners'][0]['emailAddress'])
        aux.append(a['shared'])
        a['modifiedTime'] = a['modifiedTime'].replace('Z', '')
        aux.append(datetime.strptime(a['modifiedTime'], '%Y-%m-%dT%H:%M:%S.%f'))

        return aux

    def order_data(self, a, fileExtension):
        aux = []

        aux.append(a['id'])
        aux.append(a['name'])
        aux.append(fileExtension[0]['fullFileExtension'])
        aux.append(a['owners'][0]['emailAddress'])
        aux.append(a['shared'])
        a['modifiedTime'] = a['modifiedTime'].replace('Z', '')
        aux.append(datetime.strptime(a['modifiedTime'], '%Y-%m-%dT%H:%M:%S.%f'))

        return aux

    def insert_data_user(self, args, fileExtension):
        cnx = self.get_connector()
        aux = []

        try:
            cursor = cnx.cursor()

            for a in args:
                if len(fileExtension) > 1:
                    aux = self.orderdata(a)
                else:
                    aux = self.order_data(a, fileExtension)
                cursor.callproc('sp_InsertData', aux)
                cnx.commit()
        except Exception as e:
            print(e)
        finally:
            cnx.close()

    def get_emails(self):
        cnx = self.get_connector()
        emails = []

        try:
            cursor = cnx.cursor()
            cursor.callproc('sp_GetAllUsers')

            for r in cursor.stored_results():
                for i in r:
                    emails.append(i[0])
        except Exception as e:
            print(e)
        finally:
            cnx.close()

        return emails

    def get_files(self, ownr):
        cnx = self.get_connector()
        files = []

        try:
            cursor = cnx.cursor()
            cursor.callproc('sp_GetFilesName', ownr)

            for r in cursor.stored_results():
                for i in r:
                    files.append(i[0:2])
        except Exception as e:
            print(e)
        finally:
            cnx.close()

        return files

    def update_date_file(self, args):
        cnx = self.get_connector()

        try:
            cursor = cnx.cursor()

            cursor.callproc('sp_UpdateDateModi', args)
            cnx.commit()
        except Exception as e:
            print(e)
        finally:
            cnx.close()
