skates = []
legs = []
count_wins = 0
count_skates = int(input('Кол-во коньков: '))
for _ in range(1, count_skates + 1):
    item = int(input('Размер ' + str(_) + '-й пары: '))
    skates.append(item)
count_legs = int(input('Кол-во людей: '))
for _ in range(1, count_legs + 1):
    item = int(input('Размер ноги ' + str(_) + '-го человека: '))
    legs.append(item)
for human in range(count_legs):
    standart_skates = list(skates)
    min_skates = 0
    min_skates_index = 0
    while len(standart_skates) != 0:
        min_skates = min(standart_skates)
        min_skates_index = standart_skates.index(min_skates)
        standart_skates.pop(min_skates_index)
    if min_skates >= legs[human]:
        count_wins += 1
        skates.remove(min_skates)
print('Наибольшее кол-во людей, которые могут взять ролики:', count_wins)
