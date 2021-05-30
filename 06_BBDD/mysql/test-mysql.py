import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="curso_python"
)

cursor = database.cursor(buffered=True)
cursor.execute("CREATE DATABASE IF NOT EXISTS curso_python")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehicle(
    id int(255) auto_increment not null,
    brand varchar (255) not null,
    model varchar (255) not null,
    price float(10,2) not null,
    CONSTRAINT pk_vehicle PRIMARY KEY(id))
""")
"""
cursor.execute("INSERT INTO vehicle VALUES(null, 'Opel', 'Astra', 18500.99)")
database.commit()

vehicles = [
    ('Seat', 'IBIZA', 5000.99),
    ('Renault', 'Clio', 15500.99),
    ('Citroen', 'Saxo', 2000.99),
    ('Mercedes', 'Clase C', 38500.99)
]
cursor.executemany("INSERT INTO vehicle VALUES(null, %s,%s,%s)", vehicles)
database.commit()
"""
cursor.execute("SELECT * FROM vehicle")
result = cursor.fetchall()
print(result)

cursor.execute("DELETE FROM vehicle")
cursor.close()