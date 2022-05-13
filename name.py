import mysql.connector as db
from mysql.connector import Error

try:
    connection = db.connect(host='localhost', database='comics', user='root', password='root')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        query = ("SELECT * FROM studio;")
        cursor.execute(query)
        for (id, name) in cursor:
            print("Studio: {}. {}".format(id, name))
        jmeno = input("name=")
        zbran = input("weapon=")
        studioIdx = int(input("studio(index)="))       
        insert=connection.cursor()
        code=f"INSERT INTO charact (name, weapon, studio_id) values (\"{jmeno}\", \"{zbran}\", \"{studioIdx}\")"
        print(code)
        insert.execute(code)
        connection.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")

