# scope
Username="admin"
def func1():
    Username="user"
    print(Username) # user
func1()
print(Username) # admin


y=99
# def func2(y):
#     z=x+y
#     return z

# result=func2(1)
# print(result) # 100


# def func3():
#     global x
#     x=100
#     print(x) # 100
# func3()
# print(x) # 100

def func4():
    y=88
    def func5():
        print(y) 
    return func5
result =func4()
result()
# C losure
def coder(n):
    def ac_func(x):
        return x**n
    return ac_func
 
def coder(n):
    def ac_func(x):
        return x**n
    return ac_func


f=coder(2)
g=coder(3)
print(f(3))
print(g(3))