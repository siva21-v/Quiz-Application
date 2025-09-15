import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",          
        password="Siva@2003",  
        database="quiz_system"
    )

try:
    db = connect_db()
    print("Connection successful!")
    db.close()
except Exception as e:
    print("Connection failed:", e)
