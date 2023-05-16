import functools
from typing import Optional, Callable
from datetime import datetime
import time


def log_methods(_func: Optional[Callable] = None, *, date_format: str = 'd.m.y (H:M:S)') -> Callable:
    def super_wrapped(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            date_format_directives = ''.join(f'%{symbol}' if symbol.isalpha() else symbol for symbol in list(date_format))
            start_date = datetime.utcnow()
            start = time.time()
            print(f"- Запускается '{func.__name__}'. Дата и время запуска: {start_date.strftime(date_format_directives)}")
            result = func(*args, **kwargs)
            end = time.time()
            print(f"- Завершение '{func.__name__}', время работы = {round(end - start, 3)}s ")
            return result
        return wrapped
    if _func is None:
        return super_wrapped
    return super_wrapped(_func)


def for_all_methods(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorate(cls):
        for method_name in dir(cls):
            if method_name.startswith('__') is False:
                method = getattr(cls, method_name)
                decorated_method = decorator(method)
                setattr(cls, method_name, decorated_method)
        return cls
    return decorate


@for_all_methods(log_methods(date_format="b d Y - H:M:S"))
# @for_all_methods(log_methods)
class A:
    # @log_methods(date_format="b d Y - H:M:S")
    # @log_methods
    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@for_all_methods(log_methods(date_format="b d Y - H:M:S"))
class B(A):
    # @log_methods(date_format="b d Y - H:M:S")
    def test_sum_1(self) -> None:
        super().test_sum_1()
        print("Тут метод test_sum_1 у наследника")

    # @log_methods(date_format="b d Y - H:M:S")
    def test_sum_2(self) -> int:
        print("Тут метод test_sum_2 у наследника")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
