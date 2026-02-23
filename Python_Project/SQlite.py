import sqlite3

conn =  sqlite3.connect('videos.db')

cursor= conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
               )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    print("\n")
    print("*" * 50)
    print("\n")
    for row in cursor.fetchall():
        print(row)
    print("\n")
    print("*" * 50)
   
    
def add_video(name , time):
    cursor.execute("INSERT INTO videos (name , time) values( ?, ?)" , (name , time))
    conn.commit()
    
def update_vidoe(index, name , time):
    cursor.execute("UPDATE videos SET name = ? , time = ?  WHERE id =?", (name , time , index))
    conn.commit()
    
def delete_video(index):
    cursor.execute("DELETE FROM videos where id= ? ", (index ,))
    conn.commit()
    
def main():
    while True : 
        print("YouTube MAnager | choose option")
        print("1. List of all videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("Enter Choise : ")
    
        match choice:
            case '1' :
                list_videos()
            case '2' : 
                name = input("Enter name : ")
                time = input("Enter time : ")
                add_video(name , time)
            case '3' :
                index = input("Enter input Id to update: ")
                name = input("Enter new name: ")
                time = input("Enter new time : ")
                update_vidoe(index , name , time)        
            case '4' :
                index = input("Enter input Id to delete: ")
                delete_video(index)
            case '5' :
                break
            case _ :
                print("Invalid Choise")  
    
    
    conn.close()    

if __name__ == "__main__":
    main()