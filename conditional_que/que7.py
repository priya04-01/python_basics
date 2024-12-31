#Coffee Customization
coffee_size = input("What size of coffee would you like? ")
extra_shot = input("Would you like an extra shot? ")
if extra_shot.lower()=="yes":
    print(coffee_size+" coffee with an extra shot.")
else:
    print(coffee_size+" coffee")
