import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    Data=response.json()
    if Data["success"] and "data" in Data:
     user_data=Data["data"]
     username=user_data["login"]["username"]
     country=user_data["location"]["country"]
     return username,country
    else:
       raise Exception("Failed to fetch the data")

def main():
    try:
        username,country=fetch_random_user()
        print(f"Username: {username}\nCountry: {country}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
      print("Program finished")

if __name__ =="__main__":
    main()