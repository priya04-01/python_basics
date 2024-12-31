tea_varities=["masala","ginger","green","black","mint"]
print(tea_varities) #['masala', 'ginger', 'green', 'black', 'mint']
print(tea_varities[3]) # black
print(tea_varities[1:3])#['ginger', 'green']
print(tea_varities[:4])#['masala', 'ginger', 'green', 'black']
print(tea_varities[3]) #black
tea_varities[3]="herbal"
print(tea_varities)#['masala', 'ginger', 'green', 'herbal', 'mint']
tea_varities[1:2]="lemon"
print(tea_varities)#['masala', 'l', 'e', 'm', 'o', 'n', 'green', 'herbal', 'mint']
tea_varities=["masala","ginger","green","black","mint"]
tea_varities[1:2] =["lemon"]
print(tea_varities) #['masala', 'lemon', 'green', 'black', 'mint']
print(tea_varities[1:1])
tea_varities[1:1]=["test", "test"]
print(tea_varities)#['masala', 'test', 'test', 'lemon', 'green', 'black', 'mint']
print(tea_varities[1:3])
tea_varities[1:3]=[]
print(tea_varities) #['masala', 'lemon', 'green', 'black', 'mint']
for tea in tea_varities:
        print(tea, end=" tea\n")

if "oolong" in tea_varities: 
    print("i have oolong tea")
tea_varities.append("oolong")
print(tea_varities)#['masala', 'lemon', 'green', 'black', 'mint', 'oolong']

if "oolong" in tea_varities: 
    print("i have oolong tea")
print(tea_varities.pop())    
print(tea_varities)
tea_varities.insert(3,"chocolate")
print(tea_varities)
tea_varities.remove("chocolate")
print(tea_varities)
tea_varities_copy=tea_varities.copy()# create different reference
tea_varities_copy.pop()
print(tea_varities_copy)
print(tea_varities)
#list comprehension
squared_nums=[x**2 for x in range(1,10)]
print(squared_nums)