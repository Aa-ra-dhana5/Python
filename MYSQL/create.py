import mysql.connector

#method 1

#create
conn= mysql.connector.connect(
        user = 'root' , 
        password='123456' , 
        host = 'localhost', 
        port=3306
    )
try:   
    #check
    
   if(conn.is_connected()):
       print("MySQl connected successfully!")
except:
    print('MySQL is not connected')
  

#close
conn.close()
    
'''
is_connected() - this method is used to check if the connection to ySQL is established or not
'''
  
#method 2
# config={
#     'user' : 'root',
#     'password' : '123456',
#     'host' : 'localhost',
#     'port' : 3306
# }
    
# conn = mysql.connector.connect(**config)
    
    
    
    

