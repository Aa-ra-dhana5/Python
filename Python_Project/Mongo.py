from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://admin:admin@cluster0.9atd5ja.mongodb.net/")

db = client["data"]
video_Collection = db["videos"]

# print(video_Collection)

def list_videos():
    print('\n')
    print("*" * 30)
    print('\n')
    for vid in video_Collection.find():
        print(f"ID : {vid['_id']} , Name: {vid['name']}")
    print('\n')
    print("*" * 30)
    
def add_video(name , time):
    video_Collection.insert_one({"name": name , "time" : time})

def update_vidoe(index , name , time):
    video_Collection.update_one(
        {'_id' : ObjectId(index)},
        {'$set' :{"name": name , "time": time}}
    )

def delete_video(index):
    video_Collection.delete_one({"_id": ObjectId(index)}) 

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
                print("Invalid Choice")  
        

if __name__ == "__main__":
    main()