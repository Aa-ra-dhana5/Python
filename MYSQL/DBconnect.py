import mysql
import mysql.connector



try:
    conn = mysql.connector.connect(
        user = 'root' , 
        password = '123456', 
        host = 'localhost' , 
        database= 'PythonDB',
        port =3306
    )
    if(conn.is_connected()):
        print("MySQl is connected")
        
except:
    print("MySQL is not connected")
    
sql = "CREATE TABLE client ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL)"
sql1 = "SELE.CT * FROM client"
myc = conn.cursor()
myc.execute(sql1)
for t in myc:
    print('in loop')
    print(t)




myc.close()
conn.close()