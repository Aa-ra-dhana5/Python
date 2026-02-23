#Cache Return Values
# Implement a decorator that caches the retirn values of a function so that when its called with the samea rguments, the cached calue is returned instead of re-executig the function

import time

def cache(func):
    cache_Cal = {}
    print(cache_Cal)
    def wrapper(*args):
        if args in cache_Cal:
            return cache_Cal[args]
        result = func(*args)
        cache_Cal[args] =result
        return result
    return wrapper


@cache
def long_ruFun(a, b):
    time.sleep(4)
    return a+b

print(long_ruFun(4 , 3))
print(long_ruFun( 4, 3))