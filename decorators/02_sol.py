# Debbuging Function Calls
# Create a decorator to print the function name and the values of its arguments every time in the function

def debug(func):
    def wrapper(*args, **kwargs):
        args_value =','.join(str(arg) for arg in args)
        kwargs_values = ','.join(f"{key}={value}" for key,value in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_values} ")
        return func(*args,**kwargs)
    return wrapper
@debug
def greet(name,greeting="hello"):
    print(f"{greeting}   {name}")

greet("test1","test1")
greet("test2","greetings=hello")