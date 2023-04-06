import random


class Warrior:
    health = 100
    damage = 20

    def attack(self, opponent):
        opponent.health -= self.damage
        print(f'{self.name} атаковал. У {opponent.name} осталось {opponent.health} очков здоровья')

    def __init__(self, name):
        self.name = name


def get_winner(unit_1, unit_2):
    tuple_units = (unit_1, unit_2)
    return max(tuple_units, key=lambda unit: unit.health)


def fight(unit_1, unit_2):
    while unit_1.health > 0 and unit_2.health > 0:
        order = random.randint(1, 2)
        if order == 1:
            unit_1.attack(unit_2)
        else:
            unit_2.attack(unit_1)
    winner = get_winner(unit_1, unit_2)
    print(f'Победу одержал {winner.name}!')


unit_1 = Warrior('Воин 1')
unit_2 = Warrior('Воин 2')

fight(unit_1, unit_2)
