# TODO здесь писать код

first = float(input('Введите первое положительное вещественное число: '))
second = float(input('Введите второе положительное вещественное число: '))


def getReverseStr (str):
    return ''.join(reversed(str))


def getReverseNumbers (number):
    breakNumber = str(number).split('.')
    reversedBreakNumber = map(getReverseStr, breakNumber)
    reversedNumber = '.'.join(reversedBreakNumber)
    return float(reversedNumber)


reversedFirst = getReverseNumbers(first)
reversedSecond = getReverseNumbers(second)

print('Первое число наоборот:', reversedFirst)
print('Второе число наоборот:', reversedSecond)
print('Сумма:', reversedFirst + reversedSecond)
