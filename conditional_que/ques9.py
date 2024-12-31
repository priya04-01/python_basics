#Leap year Checker
year=int(input("Enter the year: "))
# if year%4==0:
#     if year%100==0 and year %400==0:
#         print(year , " is a leap year ")
#     elif year%100==0 and year%400!=0:
#         print(year ," is not a leap year")
#     else:
#         print(year ," is a leap year")
# else:
#     print(year ," is not a leap year")

if year%4==0 and year%100!=0 or year%400==0:
    print(year," is Leap year") 
else :
    print(year, " is not a leap year")