count_records = int(input('Сколько записей вносится в протокол? '))
players = []

print('Записи (результат и имя):')
for _ in range(count_records):
    player = tuple(reversed(input(f'''{str(_ + 1)}-я запись: ''').split()))
    players.append(player)

records = [None, None, None]
record = {
    'name': '',
    'score': 0,
}

for indexr, valuer in enumerate(records):
    for index, value in enumerate(players):
        if int(value[1]) > record['score']:
            record['name'] = value[0]
            record['score'] = int(value[1])
    records[indexr] = record
    players = list(filter(lambda x: x[0] != record['name'], players))
    record = {
        'name': '',
        'score': 0,
    }

print('Итоги соревнований:')
for index, value in enumerate(records):
    print(f"{index + 1}-е место. {value['name']} ({value['score']})")

