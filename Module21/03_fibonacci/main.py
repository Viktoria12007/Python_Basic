num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))


def fibonachi(num):
    if num == 1 or num == 2:
        return 1
    fibonachi_n_minus_1 = fibonachi(num - 1)
    fibonachi_n_minus_2 = fibonachi(num - 2)
    return fibonachi_n_minus_1 + fibonachi_n_minus_2


print(fibonachi(num_pos))
