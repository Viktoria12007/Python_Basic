class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def get_info(self):
        print(f'Меня зовут {self.name}. Мне {self.age}.')
        print('У меня есть дети:')
        for child in self.children:
            print(f'  {child.name}')

    def calm_child(self, child):
        child.peace = True

    def feed_child(self, child):
        child.hunger = False


class Child:
    peace = False
    hunger = True

    def __init__(self, name, age, parent_age):
        self.name = name
        if age >= parent_age - 16:
            raise ValueError('Возраст ребёнка должен быть меньше возраста родителя хотя бы на 16 лет')
        else:
            self.age = age


child_1 = Child('Виктория', 29, 54)
child_2 = Child('Владимир', 29, 54)
print(f'Состояние спокойствия ребёнка {child_1.name}: {child_1.peace}')
print(f'Состояние голода ребёнка {child_2.name}: {child_2.hunger}')

mother = Parent('Ирина', 54, [child_1, child_2])
mother.get_info()

mother.calm_child(child_1)
mother.feed_child(child_2)
print(f'Состояние спокойствия ребёнка {child_1.name} после действия родителя {mother.name}: {child_1.peace}')
print(f'Состояние голода ребёнка {child_2.name} после действия родителя {mother.name}: {child_2.hunger}')
