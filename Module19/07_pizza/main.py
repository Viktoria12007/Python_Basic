count_orders = int(input('Введите количество заказов: '))
order_dict = dict()
for _ in range(count_orders):
    order_str = input(str(_ + 1) + ' заказ: ')
    order_arr = order_str.split()
    if order_arr[0] not in order_dict:
        order_dict[order_arr[0]] = {order_arr[1]: int(order_arr[2])}
    else:
        if order_arr[1] not in order_dict[order_arr[0]]:
            order_dict[order_arr[0]][order_arr[1]] = int(order_arr[2])
        else:
            order_dict[order_arr[0]][order_arr[1]] += int(order_arr[2])
for customer in sorted(order_dict):
    print(customer + ':')
    for pizza in sorted(order_dict[customer]):
        print('\t', pizza + ':', order_dict[customer][pizza])
