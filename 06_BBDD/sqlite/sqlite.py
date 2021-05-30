import sqlite3

#conexion
conexion = sqlite3.connect("bbdd.db")
cursor = conexion.cursor()

#create table
cursor.execute("""CREATE TABLE IF NOT EXISTS product(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title VARCHAR(255),
               description TEXT,
               price int(255));""")
#save
conexion.commit()

#insert
"""
cursor.execute("INSERT INTO product VALUES (null, 'first_product', 'description product', 56)")
conexion.commit()
"""
products = [("Computer", "15", 800),
            ("Mobile", "Android", 200),
            ("Tablet", "Android", 300)]
cursor.executemany("INSERT INTO product VALUES (null, ?, ?, ?)", products)
conexion.commit()

#delete
#cursor.execute("DELETE FROM product")

#show data
cursor.execute("SELECT * FROM product")
my_product = cursor.fetchall()
print(my_product) #tuple

#close conexion
conexion.close()