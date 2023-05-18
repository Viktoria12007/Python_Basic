import functools
from typing import Callable


def decorator_with_args_for_any_decorator(decorator_for_decoration: Callable) -> Callable:
    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            res = decorator_for_decoration(func, *args, **kwargs)
            return res
        return decorator_wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print(f'Переданные арги и кварги в декоратор: {dec_args}, {dec_kwargs}')
        result = func(*func_args, **func_kwargs)
        return result
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
decorated_function("Юзер2", 102)
