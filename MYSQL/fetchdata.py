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
    
sql = "SELECT * FROM client"
sql1 = "SELECT * FROM client where id=1"

myc = conn.cursor()
myc1 = conn.cursor(buffered=True)#loads all the data but shows only asked values
try:
    myc.execute(sql1)
    # myc1.execute(sql)
    row = myc.fetchone()
    while row is not None:
        print(row)
        row = myc.fetchone()
    
    # rows =myc.fetchall()
    # for r in rows:
    #     print(r)
    
    # rowws = myc1.fetchmany(1)
    # for rs in rowws:
    #     print(rs)
except:
    conn.rollback()
    print('unable to commit')
    
    
print("Rows affected:", myc1.rowcount)
# print("Rows affected:", myc.rowcount)

myc.close()
myc1.close()
conn.close()