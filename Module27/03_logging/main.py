import functools
import datetime
from typing import Callable, Any


def logging(func: Callable) -> Callable:
    """"
        Декоратор logging.
        Выводит имя и документацию декорируемой функции. Также записывает все ошибки
        в файл function_errors.log.
        :param func: передаётся функция, которую нужно задекорировать
        :type func: Function
        :return: wrapped_func
        :rtype: function
     """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        """
            Функция - обертка
            :param args:
            :param kwargs:
            :return: value
            :rtype: function
        """
        name_func = func.__name__
        print(f'Имя функции: {name_func}')
        print(f'Документация: {func.__doc__}')
        try:
            value = func(*args, **kwargs)
            return value
        except Exception as error:
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                file.write(f'{name_func} ({datetime.datetime.now(datetime.timezone.utc)}): {error}\n')
    return wrapped_func


@logging
def test() -> None:
    """
        Проверка декоратора и вывод простого сообщения
        :return: None
        :rtype: None
    """
    raise ValueError("ValueError")
    print('<Тут что-то происходит...>')


test()
