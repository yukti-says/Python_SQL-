<<<<<<< HEAD
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yuktisql",
    database="student_db"
)

cursor = conn.cursor()

# Insert
cursor.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", ("Yukti", 20, "Data Science"))
conn.commit()

# Read
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Update
cursor.execute("UPDATE students SET age = 21 WHERE name = 'Yukti'")
conn.commit()
for row in cursor.fetchall():
    print(row)


# Delete
cursor.execute("DELETE FROM students WHERE name = 'Yukti'")
conn.commit()

for row in cursor.fetchall():
    print(row)

conn.close()
=======
import mysql.connector as mc
from mysql.connector import Error
import pandas as pd

# creating a function for creating server
def create_server_connection(host_name ,user_name , user_password ):
    connection = None
    try:
        connection = mc.connect(
            host = host_name,
            user = user_name,
            password = user_password
        )
        print("Mysql database connected!")

    except Error as err:
        print(f"Error: '{err}' ")

    return connection   

pw = 'yuktisql'
database_name = 'work'
connection = create_server_connection("localhost","root",'yuktisql')
            
>>>>>>> 6b470e5 (Created notebook)
