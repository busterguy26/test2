import functools
import sys
# from typing import IO

text = ""
f2 = open("test.txt", "a")


# Option #1
def trace(handle):
    @functools.wraps(handle)
    def decorator(func):
        @functools.wraps(func)
        def _inner_fn(*args, **kwargs):
            print(func.__name__, args, kwargs, file=handle)
            return func(*args, **kwargs)
        return _inner_fn
    return decorator

# Option #2
# def trace(func=None, *, handle=sys.stdout):
#     if func is None:
#         return lambda func: trace(func, handle=handle)
#
#     @functools.wraps(func)
#     def inner(*args, **kwargs):
#         print(func.__name__, args, kwargs, handle)
#         return func(*args, **kwargs)
#     return inner


@trace(f2)
def num_int(num):
    """Func for transform num to integer"""
    try:
        _num = int(num)
        return _num
    except ValueError:
        return 0


print(num_int('hEllo'))
print(num_int(33))
# print(help(num_int))
