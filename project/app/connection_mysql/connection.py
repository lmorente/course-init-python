import mysql.connector

def connect():
    database = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="",
        database="curso_python",
    )
    cursor = database.cursor(buffered=True)
    return [database, cursor]