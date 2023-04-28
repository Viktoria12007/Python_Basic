import functools
import time
from collections.abc import Callable
from typing import Tuple


def slowdown(function: Callable) -> Callable:
    @functools.wraps(function)
    def wrapped_func(*args, **kwargs):
        print('Ждём 2 секунды...')
        time.sleep(2)
        print('Выполняем функцию...')
        value = function(*args, **kwargs)
        return value
    return wrapped_func


@slowdown
def slicer(list: Tuple[int, ...], number: int) -> Tuple[int, ...] | Tuple[()]:
    current_count = list.count(number)
    if current_count == 0:
        return ()
    else:
        first_appearance = list.index(number)
        if current_count == 1:
            return list[first_appearance:]
        else:
            edited_list = list[first_appearance + 1:]
            second_appearance = edited_list.index(number) + (first_appearance + 1)
            return list[first_appearance:second_appearance + 1]


list_for_check: Tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
desired_number: int = int(input('Введите искомое число: '))
print(slicer(list_for_check, desired_number))
