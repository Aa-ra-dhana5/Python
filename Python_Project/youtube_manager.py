import json

def load_video():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file) # will provide you the string not the list
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)
        
def list_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start =1): # privode indexing 
        print(f"{index}.{video['name']}, Duration:{video['time']}")
    print("\n")
    print("*" * 70)
        
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time' : time})
    save_data_helper(videos)
    
def delete_video(videos):
    list_videos(videos)
    index = int(input("Enter index of the video :  "))
    if 1<= index <=len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("video delelted succesfully")
    else:
        print("Invalid input")
    

def update_vidoe(videos):
    list_videos(videos)
    index = int(input("Enter the video number: ") )
    if 1<= index <= len(videos):
        name = input("Enter updated name: ")
        time = input("Enter updated time: ")
        videos[index-1] ={"name": name , "time": time}
        save_data_helper(videos)
    else:
        print("Invalid Input")
   
   
def main():  
    videos = load_video()  
    while True : 
        print("YouTube MAnager | choose option")
        print("1. List of all videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("Enter Choise : ")
       # print(videos)
    
        match choice:
            case '1' :
                list_videos(videos)
            case '2' : 
                add_video(videos)
            case '3' :
                update_vidoe(videos)        
            case '4' :
                delete_video(videos)
            case '5' :
                break
            case _ :
                print("Invalid Choise")    
            
            
if __name__ == "__main__" :
    main()