number = int(input('Введите num: '))


def get_order_numbers(number, count=0):
    count += 1
    print(count)
    if count < number:
        get_order_numbers(number, count)


get_order_numbers(number)
