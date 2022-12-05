list_for_check = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
desired_number = int(input('Введите искомое число: '))


def slicer(list, number):
    current_count = list.count(number)
    if current_count == 0:
        return ()
    else:
        first_appearance = list.index(number)
        if current_count == 1:
            return list[first_appearance:]
        else:
            edited_list = list[first_appearance + 1:]
            second_appearance = edited_list.index(number) + (first_appearance + 1)
            return list[first_appearance:second_appearance + 1]


print(slicer(list_for_check, desired_number))
