# Pet Food recommmendation 
pet=input("Enter the pet: ")
age=int(input("Enter the age of the pet: "))
if pet.lower()=="dog":
    if age<2:
        print("Puppy food")
    else:
        print("dog food")
elif pet.lower()=="cat":
    if age<5:
        print("Kitten food")
    else:
        print("Senior cat food")
else:
    print("Invalid pet")