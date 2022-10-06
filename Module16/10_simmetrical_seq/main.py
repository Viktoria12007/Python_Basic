count_numbers = int(input('Кол-во чисел: '))
numbers = []
stop_index = 0
for _ in range(count_numbers):
    number = int(input('Число: '))
    numbers.append(number)
print('Последовательность:', numbers)
for number in range(count_numbers - 1, -1, -1):
    if numbers[number] != numbers[number - 1]:
        stop_index = number - 1
        break
add_numbers = numbers[:stop_index + 1]
print('Нужно приписать чисел:', len(add_numbers))
print('Сами числа:', list(reversed(add_numbers)))
