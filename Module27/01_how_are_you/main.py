import functools
from typing import Callable, Any


def how_are_you(function: Callable) -> Callable:
    @functools.wraps(function)
    def wrapped_func(*args, **kwargs) -> Any:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        value = function(*args, **kwargs)
        return value
    return wrapped_func


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


test()
