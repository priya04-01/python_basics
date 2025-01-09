import json
# load data from file
def load_data(): 
    try:
        with open('youtube.txt', 'r') as file: 
            content = file.read() 
            if not content.strip(): 
                return [] 
            data = json.loads(content) 
        return data 
    except FileNotFoundError: 
        return [] 
# function to save data
def save_data(videos):
    try: 
        with open('youtube.txt', 'w') as file: 
            json.dump(videos,file) 
    except IOError as e: 
        print(f"An error occurred while saving the file: {e}")
    finally: 
        print("Data saved successfully.") 
# list the videos
def List_all_youtube_videos(videos):
    print("List of videos:\n")
    print("*" * 20)
    for index,video in enumerate(videos,start=1):
        print(f"{index}.{video['name']}, Duration: {video['time']}")
    print("\n")
# To add a new video info
def add_video(videos):
    video = input("Enter the video name: ")
    time=input ("Enter video time: ")
    videos.append({'name' :video ,'time' :time})
    save_data(videos)
    print("Video added successfully")
    return videos
# to Change the description of a video
def update_video_list(videos):
    List_all_youtube_videos(videos)
    index = int(input("Enter the index of the video to update: "))
    if 1<=index<=len(videos):
        name = input("Enter the new video name: ")
        time=input("Enter the time: ")
    videos[index-1] = {'name' :name,'time':time}
    save_data(videos)
    print("Video updated successfully")
    return videos
# to delete a video from list
def delete_video(videos):
    List_all_youtube_videos(videos)
    index = int(input("Enter the index of the video to delete: "))
    if index in range(1,len(videos)):
        print(f"{index+1}. {videos[index]}")
        videos.pop(index-1)
        print("Video deleted successfully")
        save_data(videos)
    else:
        print("INVALID OPTION")
    return videos
# Main Function 
def main():
        videos = load_data()

        while True:
            print("Welcome to the Youtube Video Manager,choose an option")
            print("1.List all youtube videos")
            print("2. Add a video")
            print("3. update the video list")
            print("4. deleta a video")
            print("5. Exit")
            option = input("Enter your choice: ")

            match option:
                case'1':
                    List_all_youtube_videos(videos)
                case '2':
                    add_video(videos)
                case '3':
                    update_video_list(videos)
                case '4':
                    delete_video(videos)
                case '5':
                    break
                case _:
                    print("Invalid option")

if __name__ == "__main__":
    main()