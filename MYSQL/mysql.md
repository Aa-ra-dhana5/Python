# Database

1.Create -- using connector.connect()
2.check  -- is_connected()
3.close --close()

---- cursor() method
this method is used to create cursor class object
we need cursor object so we call the execute() method.

it can have arguments
1.buffered = true ---> it usefull when queries return small result sets. buffered canbe used alone or in combination with the dictionary 

2.dictionary= true  -- return rows as dictionary
3. named_tup;e = true --return rows as tuple
4. prepared =true -- the cursor is used for executong preapared statements



---execute() is used to execute SQL queries

-- close() to close cursore -- remove cursor object refrence


--fetchall()
 --Fetches ALL remaining rows

--fetchmany(size)
 --Fetches only specified number of rows
  -- if you are using fetchmany() and do close the connection before fetching all the data it will show error
  --so insted use fetchall()
  -- or use buffred cursor 




Prepared Statement 
-- is used to execute the same satatemtent repeatedly with high efficiency.
-- execution cosistes of teo stages: prepare adn execute.



Prepared Statement vs Parameterized Query
--Parameterized Query → Safe way to write SQL (Coding technique)
--Prepared Statement → Performance + security mechanism in DB (Database feature)


--In mysql.connector, when you use:
   cursor.execute(sql, values)
--It automatically uses prepared statements internally.
--So in Python (mysql-connector):
--Parameterized query = Prepared statement (internally)