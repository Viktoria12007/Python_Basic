# TODO здесь писать код

number = int(input('Введите целое положительное число: '))


def get_count_numbers(number):
    return len(str(number))


def get_sum_numbers(number):
    sum = 0
    for simbol in str(number):
        sum += int(simbol)
    return sum


count_numbers = get_count_numbers(number)
sum_numbers = get_sum_numbers(number)

print('Сумма чисел:', sum_numbers)
print('Количество цифр в числе:', count_numbers)
print('Разность суммы и количества цифр:', sum_numbers - count_numbers)