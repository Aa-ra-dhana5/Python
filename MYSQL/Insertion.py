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
    
sql = "INSERT INTO client VALUES (3, 'suhani'),(4,'naina')"

delsql = "DELETE FROM client where id = 4"

updatesql = "UPDATE client SET name='radha' WHERE id=3 "
myc = conn.cursor()
try:
    myc.execute(updatesql)
    conn.commit()
except:
    conn.rollback()
    
    
print("Rows affected:", myc.rowcount)
print("last added column:", myc.lastrowid)




myc.close()
conn.close()