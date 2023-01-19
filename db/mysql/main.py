from dotenv import load_dotenv
import os
load_dotenv()


import mysql.connector



# NOTE:ただの練習なので最適なのは無視で
try:
    db = mysql.connector.connect(host='127.0.0.1', user='root', password=os.environ.get('MYSQL_PASSWORD'), database='test_mysql_database')
    cursor = db.cursor()
except:
    db = mysql.connector.connect(host='127.0.0.1', user='root', password=os.environ.get('MYSQL_PASSWORD'))
    cursor = db.cursor()
    cursor.execute('CREATE DATABASE test_mysql_database')

try:
    cursor.execute('CREATE TABLE persons('
        'id int NOT NULL AUTO_INCREMENT,'
        'name varchar(14) NOT NULL,'
        'PRIMARY KEY(id))'
        )
except: pass

cursor.execute('INSERT INTO persons(name) values("test")')
db.commit()

cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)

cursor.execute('UPDATE persons SET name = "new_name" WHERE name = "test"')

cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)
    
cursor.execute('DELETE FROM persons WHERE name = "test"')

cursor.close()
db.close()