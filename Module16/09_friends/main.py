count_friends = int(input('Кол-во друзей: '))
friends = []
for _ in range(count_friends):
    friends.append(0)
count_notes = int(input('Долговых расписок: '))
for note in range(1, count_notes + 1):
    print(str(note) + '-я расписка')
    debtor = int(input('Кому: '))
    creditor = int(input('От кого: '))
    money = int(input('Сколько: '))
    friends[debtor - 1] -= money
    friends[creditor - 1] += money
print('Баланс друзей:')
for friend in range(count_friends):
    print(str(friend + 1) + ':', friends[friend])
