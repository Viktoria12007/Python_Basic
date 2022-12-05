list1 = 'abcde'
list2 = (10, 20, 30, 40)


def my_zip(list1, list2):
    if len(list1) != len(list2):
        min_length = min(len(list1), len(list2))
    else:
        min_length = len(list1)
    return ((list1[index], list2[index]) for index in range(min_length))


generator = my_zip(list1, list2)
print('Результат:')
print(generator)
for pair in generator:
    print(pair)
