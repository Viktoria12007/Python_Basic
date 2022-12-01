import random

max_number = int(input('Введите максимальное число: '))
right_answer = {str(random.randint(1, max_number))}
right_numbers = {'0'}
wrong_numbers = {'0'}
while True:
    assumption = input('Нужное число есть среди вот этих чисел: ')
    if assumption == 'Помогите!':
        print('Артём мог загадать следующие числа:', end=' ')
        for number in list(right_numbers - wrong_numbers):
            print(number, end=' ')
        break
    estimated_numbers = set(assumption.split())
    if right_answer & estimated_numbers == right_answer:
        right_numbers.update(estimated_numbers)
        print('Ответ Артёма: Да')
    else:
        wrong_numbers.update(estimated_numbers)
        print('Ответ Артёма: Нет')
