import random


def open_a_file(name_file):
    return open(name_file, 'a')


def get_probability():
    return random.randint(1, 13)


def input_numbers():
    sum_numbers = 0
    file = open_a_file('out_file.txt')
    try:
        while sum_numbers < 777:
            number = int(input('Введите число: '))
            if get_probability() == 13:
                print('Вас постигла неудача!')
                raise ValueError
            file.write(f'{number}\n')
            sum_numbers += number
    finally:
        file.close()
    print('Вы успешно выполнили условие для выхода из порочного цикла!')


input_numbers()
