len_list = int(input('Введите длину списка: '))
result = [1 if number % 2 == 0 else number % 5 for number in range(len_list)]
print('Результат:', result)
