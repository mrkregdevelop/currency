from time import sleep, time

CACHE = {}

'''
LEGB

L - local
E - enclosure
G - global
B - builtins (len, print, int, bool)

__hash__


'''


# def slow(n, a):
#     global CACHE
#
#     key = f'{n}::{a}'
#
#     if key in CACHE:
#         return CACHE[key]
#
#     sleep(n + a)  # some calculations
#     result = n ** 2 + a
#     CACHE[key] = result
#
#     return result

def cache_func(function):
    def wrapper(*args, **kwargs):
        key = f'{function.__name__}::{args}::{kwargs}'
        print(key)

        if key in CACHE:
            return CACHE[key]

        sleep(5)

        result = function(*args, **kwargs)

        CACHE[key] = result

        return result

    return wrapper


@cache_func
def add(x, y):
    return x + y


@cache_func
def foo():
    return 1


start = time()
print(add(12, 3))
print(add(12, 3))
print(foo())
print(foo())

print(CACHE)
print(f'Time: {time() - start}')
