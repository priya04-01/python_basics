import requests

def create_joke():
    url="https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response=requests.get(url)
    data=response.json()
    if data["success"] and "data" in data:
        user_data=data["data"]
        joke=user_data["content"]
        return joke
    else:
        raise Exception ("Failed to fetch the data")
    
def main():
    try:
        joke=create_joke()
        print(f"Joke of the Day: {joke}")
    except Exception as e :
        print(f"An error {e} occurred while fetching the joke")
    finally:
        print("Thank you for listening to the joke of the day!")

if __name__=="__main__":
    main()