import mysql
import mysql.connector



try:
    conn = mysql.connector.connect(
        user = 'root' , 
        password = '123456', 
        host = 'localhost' , 
        port =3306
    )
    if(conn.is_connected()):
        print("MySQl is connected")
        
except:
    print("MySQL is not connected")
    
sql = "CREATE DATABASE PythonDB"
myc = conn.cursor()
myc.execute(sql)

myc.close()
conn.close()