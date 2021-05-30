from project.app.connection_mysql.connection import connect

connect = connect()
database = connect[0]
cursor = connect[1]

class Note():

    def __init__(self, user_id, title="", description=""):
        self.__user_id = user_id
        self.__title = title
        self.__description = description

    def get_user(self):
        return self.__user_id

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description


    def save(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        note = (self.__user_id, self.__title, self.__description)
        cursor.execute(sql, note)
        database.commit()

        return [cursor.rowcount, self]

    def find(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.__user_id}"
        cursor.execute(sql)
        database.commit()

        result = cursor.fetchall()
        return result

    def deleteByTitle(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.__user_id} AND titulo LIKE '%{self.__title}%'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]