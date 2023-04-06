class Water:
    name = 'Вода'

    def __add__(self, other):
        if other.name == 'Воздух':
            return Storm()
        elif other.name == 'Огонь':
            return Steam()
        elif other.name == 'Земля':
            return Dirt()
        else:
            print(f'Невозможно создать новый элемент из {self.name} и {other.name}!')
            return None


class Air:
    name = 'Воздух'

    def __add__(self, other):
        if other.name == 'Вода':
            return Storm()
        elif other.name == 'Огонь':
            return Lightning()
        elif other.name == 'Земля':
            return Dust()
        else:
            print(f'Невозможно создать новый элемент из {self.name} и {other.name}!')
            return None


class Fire:
    name = 'Огонь'

    def __add__(self, other):
        if other.name == 'Воздух':
            return Lightning()
        elif other.name == 'Вода':
            return Steam()
        elif other.name == 'Земля':
            return Lava()
        else:
            print(f'Невозможно создать новый элемент из {self.name} и {other.name}!')
            return None


class Ground:
    name = 'Земля'

    def __add__(self, other):
        if other.name == 'Воздух':
            return Dust()
        elif other.name == 'Огонь':
            return Lava()
        elif other.name == 'Вода':
            return Dirt()
        else:
            print(f'Невозможно создать новый элемент из {self.name} и {other.name}!')
            return None


class Storm:
    name = 'Шторм'

    def created(self):
        print(f'Создан новый элемент {self.name}!')


class Steam:
    name = 'Пар'

    def created(self):
        print(f'Создан новый элемент {self.name}!')


class Dirt:
    name = 'Грязь'

    def created(self):
        print(f'Создан новый элемент {self.name}!')


class Lightning:
    name = 'Молния'

    def created(self):
        print(f'Создан новый элемент {self.name}!')


class Dust:
    name = 'Пыль'

    def created(self):
        print(f'Создан новый элемент {self.name}!')


class Lava:
    name = 'Лава'

    def created(self):
        print(f'Создан новый элемент {self.name}!')


try:
    element_1 = Water()
    element_2 = Fire()

    element_3 = element_2 + element_1
    element_3.created()

    element_4 = element_1 + element_3
    element_4.created()
except AttributeError:
    print('Вы пытаетесь обратиться к пустому элементу!')
