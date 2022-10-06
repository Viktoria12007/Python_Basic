shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

good_name = input('Название детали: ').lower()
count_chosen_good = 0
price_chosen_good = 0
for index in range(len(shop)):
    if shop[index][0] == good_name:
        count_chosen_good += 1
        price_chosen_good += shop[index][1]
print('Название детали:', good_name)
print('Кол-во деталей —', count_chosen_good)
print('Общая стоимость —', price_chosen_good)
