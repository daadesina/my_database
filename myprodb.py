import pymysql

db = pymysql.connections.Connection(
        host='localhost',
        user='adesina',
        password='ab702810'
        )

print (db)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")

cursor.close()
db.close()
