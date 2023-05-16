import functools
from typing import Callable


def decorator_with_args_for_any_decorator(decorator_for_decoration: Callable) -> Callable:
    @functools.wraps(decorator_for_decoration)
    def wrapped_(*args, **kwargs):
        def decorator(func):
            res = decorator_for_decoration(func, *args, **kwargs)
            return res
        return decorator
    return wrapped_


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        print('start wrapped')
        result = func(*args, **kwargs)
        return result
    return wrapped


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
