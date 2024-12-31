print("chai aur python")

def chai(n):
    print(n)

chai("lemon tea")    
chai_1="lemon tea"
chai_2="ginger tea"
chai_3="masala tea"
# repr,str,print

# slicing
print(chai_1[0:3])  
# prints "lem"
print(chai_1[4:7])
# prints "tea"
num_list="0123456789"
print(num_list[:]) # 0123456789
print(num_list[3:]) #3456789
print(num_list[:7]) #0123456
print(num_list[0:7:2]) #0246
print(num_list[0:7:3])#036
print(num_list[3:-1:2]) #  357

# string methods :upper(), lower(), strip(),replace(x,y),split(" "), find(""),count("x")," , ".join(x), len()

# order formatting
bread="brown"
quantity=2
order="i ordered {} loafs of {} bread"
print(order.format(quantity,bread))