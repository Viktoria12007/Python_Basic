import random


class KillError(Exception):
    """ Класс KillError. Родитель: Exception """
    pass


class DrunkError(Exception):
    """ Класс DrunkError. Родитель: Exception """
    pass


class CarCrashError(Exception):
    """ Класс CarCrashError. Родитель: Exception """
    pass


class GluttonyError(Exception):
    """ Класс GluttonyError. Родитель: Exception """
    pass


class DepressionError(Exception):
    """ Класс DepressionError. Родитель: Exception """
    pass


def open_write(file_name, text):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(text)


def one_day():
    luck = random.randint(1, 10)
    type_error = random.randint(1, 5)
    try:
        if luck == 10:
            if type_error == 1:
                raise KillError('Вы убили!')
            elif type_error == 2:
                raise DrunkError('Вы напились!')
            elif type_error == 3:
                raise CarCrashError('Вы попали в аварию!')
            elif type_error == 4:
                raise GluttonyError('Вы объелись!')
            elif type_error == 5:
                raise DepressionError('Вы впали в дипрессию!')
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as error:
        open_write('karma.log', f'{error}\n')
    return random.randint(1, 7)


karma = 0

while karma < 500:
    karma += one_day()
