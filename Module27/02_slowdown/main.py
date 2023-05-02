import functools
import time
from typing import Callable, Any


def slowdown(function: Callable) -> Callable:
    @functools.wraps(function)
    def wrapped_func(*args, **kwargs) -> Any:
        print('Ждём 2 секунды...')
        time.sleep(2)
        print('Выполняем функцию...')
        value = function(*args, **kwargs)
        return value
    return wrapped_func


@slowdown
def test() -> None:
    print('<Тут что-то происходит...>')


test()
