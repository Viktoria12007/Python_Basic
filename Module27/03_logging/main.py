import functools
import datetime
from collections.abc import Callable
from typing import Tuple


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
    def wrapped_func(*args, **kwargs):
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
def slicer(list: Tuple[int, ...], number: int) -> Tuple[int, ...] | Tuple[()]:
    """
        Функция slicer возвращающая часть кортежа начинающего и заканчивающегося переданной цифрой.
        Если такой цифры нет в кортеже то возвращается пустой кортеж.
        Если такая цифра встречается в кортеже один раз, то возвращается часть кортежа с вхождения переданной цифры
        и до конца кортежа.
        :param list: передаётся кортеж
        :type list: tuple
        :param number: передаётся искомая цифра
        :type number: int
        :return: () | list[first_appearance:] | list[first_appearance:second_appearance + 1]
        :rtype: function
    """
    current_count = list.count(number)
    if current_count == 0:
        raise TypeError("TypeError")
        return ()
    else:
        raise IndexError("IndexError")
        first_appearance = list.index(number)
        if current_count == 1:
            return list[first_appearance:]
        else:
            edited_list = list[first_appearance + 1:]
            second_appearance = edited_list.index(number) + (first_appearance + 1)
            return list[first_appearance:second_appearance + 1]


@logging
def test() -> None:
    """
        Функция выводящая print.
        :return: None
        :rtype: None
    """
    raise ValueError("ValueError")
    print('<Тут что-то происходит...>')


list_for_check: Tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
desired_number: int = int(input('Введите искомое число: '))
print(slicer(list_for_check, desired_number))

test()
