# Validate Input
while True:
    number=int(input("enter the number: "))
    if number>0 and number<11:
     print("Correct")
     break
    else:
        print("Invalid input")
