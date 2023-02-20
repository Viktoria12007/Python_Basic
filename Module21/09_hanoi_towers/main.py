count_disk = int(input('Введите количество дисков: '))


def move(disk, from_rod, to_rod, aux_rod):
    if disk == 1:
        print(f'Переложить диск {disk} со стержня номер {from_rod} на стержень номер {to_rod}')
        return
    else:
        if disk >= 2:
            move(disk - 1, from_rod, aux_rod, to_rod)
            print(f'Переложить диск {disk} со стержня номер {from_rod} на стержень номер {to_rod}')
            move(disk - 1, aux_rod, to_rod, from_rod)


move(count_disk, 1, 3, 2)
