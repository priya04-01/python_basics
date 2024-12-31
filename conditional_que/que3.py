# Grade generator

score = int(input("Enter your score: "))
if score > 100 or score < 0:
    print("Invalid score")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#ifscore>100 or score<0 print("Invalid score")
# exit()
# elif score >= 90:
#     Grade ="A"
# elif score >= 80:
#     Grade ="B"
# elif score >= 70:
#     Grade ="C"
# elif score >= 60:
#     Grade ="D"
# else:
#     Grade ="F"
# print("Grade:",Grade)
