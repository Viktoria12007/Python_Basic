import functools
from typing import Optional, Callable


def callback(_func: Optional[Callable] = None, *, route: str = '/') -> Callable:
    def super_wrapped(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            app[route] = func
            return result
        return wrapped
    if _func is None:
        return super_wrapped
    return super_wrapped(_func)


@callback(route='//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


app = {}
example()
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
