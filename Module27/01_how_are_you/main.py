import functools
from collections.abc import Callable
from typing import Tuple


def how_are_you(function: Callable) -> Callable:
    @functools.wraps(function)
    def wrapped_func(*args, **kwargs):
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        value = function(*args, **kwargs)
        return value
    return wrapped_func


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
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


test()
print(test.__name__)

list_for_check: Tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
desired_number: int = int(input('Введите искомое число: '))
print(slicer(list_for_check, desired_number))
