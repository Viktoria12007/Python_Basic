import functools
from typing import Callable, Any


def counter(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        value = func(*args, **kwargs)
        wrapped_func.count += 1
        print(f'Количество вызовов декорируемой функции {func.__name__}: {wrapped_func.count}')
        return value
    wrapped_func.count = 0
    return wrapped_func
    # def wrapped_func(*args, **kwargs):
    #     value = func(*args, **kwargs)
    #     if hasattr(func, 'count'):
    #         func.count += 1
    #     else:
    #         func.count = 1
    #     print(f'Количество вызовов декорируемой функции {func.__name__}: {func.count}')
    #     return value
    # return wrapped_func
    # def wrapped_func(*args, **kwargs):
    #     value = func(*args, **kwargs)
    #     if func.__name__ in wrapped_func.counts:
    #         wrapped_func.counts[func.__name__] += 1
    #     else:
    #         wrapped_func.counts[func.__name__] = 1
    #     print(f'Количество вызовов декорируемой функции {func.__name__}: {wrapped_func.counts[func.__name__]}')
    #     return value
    # if not hasattr(wrapped_func, 'counts'):
    #     wrapped_func.counts = {}
    # return wrapped_func


@counter
def test() -> None:
    print('<Тут что-то происходит...>')


test()
test()
