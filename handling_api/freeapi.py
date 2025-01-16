import requests

def fetch_random_user():
    url = 'https://api.freeapi.app/api/v1/public/quotes/quote/random'
    response=requests.get(url)
    data=response.json()
    if data["success"] and "data" in data:
     user_data=data["data"]
     username=user_data["login"]["username"]
     country=user_data["location"]["country"]
     return username,country
    else:
       raise Exception("Failed to fetch the data")

def main():
    try:
        username,country=fetch_random_user()
        print(f"Username: {username}, Country: {country}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
      print("Program finished")

if __name__ =="__main__":
    main()