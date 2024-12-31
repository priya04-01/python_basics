# function with **kwargs
# function that accepts multiple arguments and print them as key: value pair
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
print_kwargs(name="John", age=25, city="New York")
print_kwargs(name="mohan")