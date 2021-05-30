import hashlib
from datetime import datetime
from project.app.connection_mysql.connection import connect

connect = connect()
database = connect[0]
cursor = connect[1]

class User():

    def __init__(self, id, name, surname, mail, password):
        self.__id = id
        self.__name = name
        self.__surname = surname
        self.__mail = mail
        self.__password = password

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_mail(self):
        return self.__mail

    def get_password(self):
        return self.__password


    def register(self):
        new_date = datetime.now()
        encrypted = hashlib.sha256()
        encrypted.update(self.__password.encode('utf8'))

        new_user = (self.__name, self.__surname, self.__mail, encrypted.hexdigest(), new_date)
        add_user = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"

        try:
            cursor.execute(add_user, new_user)
            database.commit()
            result = [cursor.rowcount, self]
        except:
           result = [0, self]

        return result

    def authenticate(self):
        encrypted = hashlib.sha256()
        encrypted.update(self.__password.encode('utf8'))
        login_user = (self.__mail, encrypted.hexdigest())

        sql = "SELECT * FROM usuarios WHERE email = %s AND contraseña = %s"
        cursor.execute(sql, login_user)
        result = cursor.fetchone()

        return result
