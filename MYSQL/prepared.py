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
    
sql = "INSERT INTO client VALUES (%s, %s)"
delsql = "DELETE FROM client WHERE id =?"
updatesql = "UPDATE client SET name = 'papita' WHERE id=?"
myc = conn.cursor(prepared=True)
params =(11, 'Ravi')
mulparams =  [(15, 'suhani'), (16, ' unil'), (17,'reva')]
try:
    # myc.execute(sql, params)
    myc.executemany(sql, mulparams)
    conn.commit()
    print('row affected: ', myc.rowcount)
    print(f'std id: {myc.lastrowid} is added') 
except:
    conn.rollback()
    print('unable to commit')


myc.close()
conn.close()