import functools
from collections.abc import Callable
from typing import Tuple


def counter(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
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


@counter
def slicer(list: Tuple[int, ...], number: int) -> None:
    current_count = list.count(number)
    if current_count == 0:
        print(())
    else:
        first_appearance = list.index(number)
        if current_count == 1:
            print(list[first_appearance:])
        else:
            edited_list = list[first_appearance + 1:]
            second_appearance = edited_list.index(number) + (first_appearance + 1)
            print(list[first_appearance:second_appearance + 1])


list_for_check: Tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
desired_number: int = int(input('Введите искомое число: '))
slicer(list_for_check, desired_number)
test()
slicer(list_for_check, desired_number)
slicer(list_for_check, desired_number)
test()
