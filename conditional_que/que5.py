# weather activity suggestion

weather = input("Enter the weather: ")
if weather.lower() == "sunny":
    print("Go for a walk")
elif weather.lower() == "rainy":
    print("Read a book")
elif weather.lower() == "snowy":
    print("Build a snowman")
else:
    print("Sorry, I'm not sure what to suggest for that weather")