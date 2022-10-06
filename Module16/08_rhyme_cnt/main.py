count_people = int(input('Кол-во человек: '))
stop_human = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', stop_human, '-й человек')
current_round = []
for human in range(1, count_people + 1):
    current_round.append(human)
start_human = 0
while len(current_round) >= 2:
    print('Текущий круг людей:', current_round)
    print('Начало счёта с номера', current_round[start_human])
    counter = stop_human
    while counter >= 1:
        for human in range(start_human, len(current_round)):
            if counter >= 1:
                counter -= 1
                start_human = 0
            else:
                start_human = human
                break
    print('Выбывает человек под номером', current_round[start_human - 1])
    current_round.pop(start_human - 1)
    if start_human == 0:
        start_human = 0
    else:
        start_human = start_human - 1
print('Остался человек под номером', current_round[0])
