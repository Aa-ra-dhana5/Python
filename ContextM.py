import sqlite3
from contextlib import contextmanager

#Class based context manager
class DBconnection:
    def __init__(self, db_path:str):
        self.db_path = db_path
        self.connection = None    
    
    def __enter__(self):
        print(f'Conneting to the database: {self.db_path}')
        self.connection =sqlite3.connect(self.db_path)
        return self.connection
    
    def __exit__(self,exc_type):
        if self.connection:
            if exc_type:
                print(f'Error Occured: Rollback')
                self.connection.rollback()
            else:
                print("Commit Changes")
                self.connection.commit()
            print('close Connection')
            self.connection.close()