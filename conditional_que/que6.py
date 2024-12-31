# Transportation Mode Selection
distance = float(input("Enter the distance to be travelled: "))
if distance < 3:
    print("I suggest you to walk.")
elif distance < 16:
    print("I suggest you to take a Bike.")
else :
    print("I suggest you to take a Car.")