import mysql.connector as mysql
       
db = mysql.connect(
    host = "localhost",
    user = "root",
    pasword = "yuktisql",
    database = "student_db"
)

curser = db.cursor()

# getting version
curser.execute("select version()")
version = curser.fetchone()[0]
print(f"Mysql version is {version}")

