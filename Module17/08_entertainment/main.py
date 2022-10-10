import random
count_sticks = int(input('Количество палок: '))
count_throws = int(input('Количество бросков: '))
sticks = ['I' for _ in range(count_sticks)]
for throw in range(count_throws):
    pair_knocked_down_sticks = sorted([random.randint(1, count_sticks), random.randint(1, count_sticks)])
    sticks = ['.' if pair_knocked_down_sticks[0] - 1 <= stick <= pair_knocked_down_sticks[1] - 1
              else sticks[stick] for stick in range(count_sticks)]
    print('Бросок', str(throw + 1) + '. Сбиты палки с номера',
          pair_knocked_down_sticks[0], 'по номер', str(pair_knocked_down_sticks[1]) + '.')
print('Результат:', sticks)
