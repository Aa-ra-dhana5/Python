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

# when data passed in tuple formate    
sql = "INSERT INTO client VALUES (%s, %s)"

#when pramr is directory
sql1 = "INSERT INTO client VALUES (%(id)s, %(name)s)"

#when data is mulple tuples
sql2 = "INSERT INTO client VALUES (%s, %s)"
params = [(5, 'om'),(6, 'arya'),(7, 'lara')]


myc = conn.cursor()
try:
    # myc.execute(sql, (2, 'Rohan'))
    myc.executemany(sql2, params)
    # myc.execute(sql1, {'id':4 , 'name':'ishan'})
    conn.commit()
except:
    conn.rollback()
    
    
print("Rows affected:", myc.rowcount)
print("last added column:", myc.lastrowid)

myc.close()
conn.close()