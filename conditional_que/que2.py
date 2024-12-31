 #2.movie ticket price
print("enter the age")
age = int(input())
if age<18 :
    ticket =8
else: 
    ticket =12
# ticket=12 ifage>=18 else 8

print("enter the day")
day = input()
if day == "wednesday":
    print("Ticket price is $",ticket-2)
else:
    print("Ticket price is $",ticket)
#if day =="wednesday" ticket-=2 print("Ticket price is $",ticket)