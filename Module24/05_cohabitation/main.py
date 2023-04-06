import random


class Human:
    fullness = 50
    death = False

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def eat(self):
        self.fullness += 1
        self.house.food -= 1
        print(f'{self.name} поел. Уровень сытости: {self.fullness}. Уровень еды: {self.house.food}')

    def work(self):
        self.fullness -= 1
        self.house.money += 1
        print(f'{self.name} поработал. Уровень сытости: {self.fullness}. Уровень денег: {self.house.money}')

    def play(self):
        self.fullness -= 1
        print(f'{self.name} поиграл. Уровень сытости: {self.fullness}.')

    def go_shopping(self):
        self.house.food += 1
        self.house.money -= 1
        print(f'{self.name} сходил в магазин за едой.  Уровень еды: {self.house.food}. Уровень денег: {self.house.money}')


class House:
    food = 50
    money = 0


def action_logic(human):
    if not human.death:
        luck = random.randint(1, 6)
        if human.fullness < 20 and house.food > 0:
            human.eat()
        elif human.house.food < 10 and house.money > 0:
            human.go_shopping()
        elif human.house.money < 50 and human.fullness > -1:
            human.work()
        elif luck == 1 and human.fullness > -1:
            human.work()
        elif luck == 2 and house.food > 0:
            human.eat()
        else:
            if human.fullness > -1:
                human.play()
        if human.fullness < 0:
            human.death = True
            print(f'{"*" * 20}{human.name} умер. Уровень сытости: {human.fullness}{"*" * 20}')


def year_life():
    day = 0
    while day < 365:
        day += 1
        print(f'{day} день')
        action_logic(human_1)
        action_logic(human_2)
        if human_1.death and human_2.death:
            break


house = House()
human_1 = Human('Виктория', house)
human_2 = Human('Игорь', house)

year_life()
