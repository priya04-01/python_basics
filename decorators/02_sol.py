# Debbuging Function Calls
# Create a decorator to print the function name and the values of its arguments every time in the function

def debug(func):
    def wrapper(*args, **kwargs):
        args_value =','.join(str(arg) for arg in args)
        kwargs_values = ','.join(f"{key}={value}" for key,value in kwargs.items())
        return func(*args,**kwargs)
    return wrapper

def greet(name,greeting="hello"):
    print(f"{greeting}   {name}")