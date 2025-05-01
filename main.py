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
