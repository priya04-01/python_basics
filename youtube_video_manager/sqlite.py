# sqlite is a c library that provides a lightweight disk-based database that doesn't require a separate server process. It allows access to the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. It's also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
import sqlite3
con=sqlite3.connect('mydatabase.db')
# con is the connection object that represents the database
# returns connection object 
cur=con.cursor()
# cur is the cursor object that allows Python code to execute SQL commands against the database and retrieve data from the database into Python variables.
result=cur.execute('''
create table if not exists videos(id integer primary key, name text not null, time text not null)
''')
def list_videos():
    result=cur.execute('select * from videos')
    for row in result:
        print(row)
def add_video(name,time):
    cur.execute('insert into videos(name,time) values(?,?)',(name,time))
    con.commit()
    print("Video added successfully")
def update_video(video_id):
    result=cur.execute('select * from videos where id=?',(video_id,))
    row = result.fetchone()
    if row:
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        result=cur.execute('update videos set name=?,time=? where id=?',(name,time,video_id))
        con.commit()
        print("Video updated successfully")
    else:
        print("No video found with the given id")
def delete_video(video_id):
    cur.execute('delete from videos where id=?',(video_id,))
    con.commit()
    print("Video deleted successfully")
    return result
def load_data():
    result=cur.execute('select * from videos')
    videos = []
    for row in result:
        videos.append({'id':row[0],'name':row[1],'time':row[2]})
    return videos
def save_data(videos):
    cur.execute('delete from videos')
    for video in videos:
        cur.execute('insert into videos(id,name,time) values(?,?,?)',(video['id'],video['name'],video['time']))
    con.commit()
    print("Data saved successfully")


def main():
    while True:
            print("Welcome to the Youtube Video Manager,choose an option")
            print("1.List all youtube videos")
            print("2. Add a video")
            print("3. update the video list")
            print("4. deleta a video")
            print("5. Exit App")
            option = input("Enter your choice: ")

            if option =='1':
                list_videos()
            elif option =='2':
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_video(name,time)
            elif option == '3':
                video_id=input("Enter the video Id : ")
                update_video(video_id)
            elif option =='4':
                video_id=input("Enter the video Id: ")
                delete_video(video_id)
            elif option =='5':
                break
            else:
                print("Invalid option")
    con.close()

if __name__ =="__main__":
    main()