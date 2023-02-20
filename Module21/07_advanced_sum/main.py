def my_sum(*args):
    if len(args) > 1:
        return multiple_arguments(args)
    else:
        if isinstance(args[0], list):
            return one_arr_argument(args[0])
        else:
            return args[0]


def multiple_arguments(numbers, current_index=0):
    if current_index >= len(numbers):
        return 0
    return numbers[current_index] + multiple_arguments(numbers, current_index + 1)


def one_arr_argument(elements):
    summ = 0
    for index, element in enumerate(elements):
        if not isinstance(element, list):
            summ += element
        else:
            summ += one_arr_argument(element)
    return summ


print(my_sum(1, 2, 3, 4, 5))
# print(my_sum([[1, 2, [3]], [1], 3]))
# print(my_sum(3))
