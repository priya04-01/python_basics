import requests

def random_meal():
    url="https://api.freeapi.app/api/v1/public/meals/meal/random"
    response=requests.get(url)
    Data=response.json()
    if Data["success"] and "data" in Data:
        user_data=Data['data']
        Meal_id=user_data["idMeal"]
        Dish_name=user_data["strMeal"]
        Instructions=user_data["strInstructions"]
        return Meal_id,Dish_name,Instructions
    else:
       raise Exception("Failed to fetch the data")

def main():
    try:
        Meal_id,Dish_name,Instructions=random_meal()
        print(f"Meal Id: {Meal_id}\nDish Name: {Dish_name}\nInstructions:{Instructions}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
      print("Program finished")

if __name__ =="__main__":
    main()