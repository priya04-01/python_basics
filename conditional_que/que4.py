# Fruit Ripeness Checker
fruit = input("Enter the name of the fruit: ")
color = input("Enter the color of the fruit: ")
if fruit.lower() == "banana":
    if color.lower()== "green":
        print("The fruit is Unripe yet.")
    elif color.lower()== "yellow":
        print("The fruit is Ripe.")
    elif color.lower() == "brown":
        print("The fruit is Overripe.")
else:
    print("The fruit is not a Banana.")