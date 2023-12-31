goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for good in goods:
    count_goods = 0
    total_price = 0
    for purchased_goods in store[goods[good]]:
        count_goods += purchased_goods['quantity']
        total_price += purchased_goods['quantity'] * purchased_goods['price']
    print('{0} — {1} штук, стоимость {2:_d} рубля'.format(good, count_goods, total_price).replace('_', ' '))
    print('{0} — {1} штук, стоимость {2:_d} рубля'.format(good, count_goods, total_price).replace('_', ' '))