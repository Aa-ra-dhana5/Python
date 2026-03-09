import mysql.connector
 
print("Script started")
 
try:
    print("Trying to connect...")
 
    conn = mysql.connector.connect(
        user='root',
        password='123456',
        host='127.0.0.0',
        port=3306
    )
 
    print("Connection object created")
 
    if conn.is_connected():
        print("MySQL is connected")
    else:
        print("Connection failed")
 
except Exception as e:
    print("Error:", e)
 
print("Program finished")