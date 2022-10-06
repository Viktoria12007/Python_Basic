first_list = []
second_list = []
first_list_unique = []
for item in range(1, 11):
    if item < 4:
        number = int(input('Введите ' + str(item) + '-е число для первого списка: '))
        first_list.append(number)
    else:
        number = int(input('Введите ' + str(item) + '-е число для второго списка: '))
        second_list.append(number)
print('Первый список:', first_list)
print('Второй список:', second_list)
first_list.extend(second_list)
first_list_unique = list(dict.fromkeys(first_list))
print('Новый первый список с уникальными элементами:', first_list_unique)
