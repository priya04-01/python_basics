#Password Strength Checker
password=input("enter the password: ")
if len(password)< 6:
    print("Weak")
elif len(password)<11:
    print("Medium")
else:
    print("Strong")