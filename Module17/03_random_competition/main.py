import random
first_team = [round(random.random() * (10 - 5) + 5, 2) for _ in range(20)]
print('Первая команда:', first_team)
second_team = [round(random.random() * (10 - 5) + 5, 2) for _ in range(20)]
print('Вторая команда:', second_team)
wins = [first_team[player] if first_team[player] > second_team[player] else second_team[player]
        for player in range(len(first_team))]
print('Победители тура:', wins)
