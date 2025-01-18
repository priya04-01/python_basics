import pymongo
client = pymongo.MongoClient("mongodb+srv://youtubepy:Pr7089819965@cluster0.meobw.mongodb.net/")
db=client["ytmanager"]
video_collection=db["videos"]

def main():
    while True:
        print("\nYoutube Manager App")
        print("1. Add Video")
        print("2. Delete Video")
        print("3. Update Video")
        print("4. Display All Videos")
        print("5. Exit")
        choice=input("Enter the choice: ")

        if choice=='1':
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            video_collection.insert_one({"name":name,"time":time})
        elif choice=='2':
            name=input("Enter the video name to delete:")
            video_collection.delete_one({"name":name})
        elif choice=='3':
            name=input("Enter the video name to update:")
            time=input("Enter the new video time:")
            video_collection.update_one({"name":name},{"$set":{"time":time}})
        elif choice=='4':
            for video in video_collection.find():
                print(f"ID: {video['_id']}\n Name: {video['name']},Time: {video['time']}")
        elif choice=='5':
            break
        else:
            print("invalid choice")

if __name__=="__main__":
    main()