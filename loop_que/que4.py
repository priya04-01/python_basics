# Reverse a String using a loop
String=str(input("Enter a string: "))
rString = ""
for char in String:
    rString=char+rString
print("\nReversed String: ", rString)