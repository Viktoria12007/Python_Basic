class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Ground):
            return Dirt()
        else:
            print(f'Невозможно создать новый элемент из {self} и {other}!')
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Ground):
            return Dust()
        else:
            print(f'Невозможно создать новый элемент из {self} и {other}!')
            return None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Ground):
            return Lava()
        else:
            print(f'Невозможно создать новый элемент из {self} и {other}!')
            return None


class Ground:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()
        else:
            print(f'Невозможно создать новый элемент из {self} и {other}!')
            return None


class Storm:
    def __str__(self):
        return 'Шторм'


class Steam:
    def __str__(self):
        return 'Пар'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Lightning:
    def __str__(self):
        return 'Молния'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


try:
    element_1 = Water()
    element_2 = Fire()

    element_3 = element_2 + element_1
    print(element_3)

    element_4 = element_1 + element_3
    print(element_4)
    print(element_4 + element_1)
except TypeError:
    print('Вы пытаетесь соединить не соединяемые элементы!')
