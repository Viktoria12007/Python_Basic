# TODO здесь писать код

number = int(input('Введите целое положительное число, которое больше единицы: '))


def getMinDivisor (number):
    if number <= 1:
        return print('Число должно быть больше 1!')
    for step in range(2, number + 1):
        if number % step == 0:
            return step


minDivisior = getMinDivisor(number)

print('Наименьший делитель, отличный от единицы:', minDivisior)
