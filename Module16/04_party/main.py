guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
limit_guests = 6
last_answer = False

while not last_answer:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    answer = input('Гость пришёл или ушёл? ').lower()
    if answer == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    elif answer == 'пришёл':
        name_guest = input('Имя гостя: ')
        if len(guests) == limit_guests:
            print('Прости,', name_guest, 'но мест нет.')
        else:
            guests.append(name_guest)
            print('Привет,', name_guest, '!')
    elif answer == 'ушёл':
        name_guest = input('Имя гостя: ')
        guests.remove(name_guest)
        print('Пока,', name_guest, '!')

