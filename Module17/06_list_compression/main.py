import random
count_numbers = int(input('Количество чисел в списке: '))
numbers = [random.randint(0, 2) for _ in range(count_numbers)]
print('Список до сжатия:', numbers)
number_without_zero = list(filter(lambda x: x != 0, numbers))
print('Список после сжатия:', number_without_zero)
