# Sum of even Numbers 
# Write a program to find the sum of all even numbers from 1 to n where n is given by the user.
number=int(input("Enter the number of elements: "))
sum=0
for num in range(1,number+1):
    if num%2==0:
        sum+=num
print("The sum of even numbers from 1 to",number,"is",sum)