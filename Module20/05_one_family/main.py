families = {
        ('Сидоров', 'Никита'): 35,
        ('Лысенко', 'Людмила'): 27,
        ('Боброва', 'Ирина'): 24,
        ('Боброва', 'Юля'): 2,
        ('Сидорова', 'Алина'): 34,
        ('Лысенко', 'Игорь'): 30,
        ('Сидоров', 'Павел'): 10,
        ('Лысенко', 'Владимир'): 4,
        ('Бобров', 'Антон'): 25,
}

surname = input('Введите фамилию: ').lower()


def getFamily(surname):
    return {' '.join(key): value for key, value in families.items()
            if key[0].lower() in surname + 'а'}


for key, value in getFamily(surname).items():
    print(key, value)
