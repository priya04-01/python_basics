# Cache return Value
# Implement a decorator that caches the return values of a function, sp that when it's called with the same arguments, the catched value is returned instead of re-executing the function
import time
def cache_return_value(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@cache_return_value
def function(a,b):
    time.sleep(4)
    return a+b

print(function(7,8))
print(function(2,3))