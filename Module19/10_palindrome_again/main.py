string = input('Введите строку: ')


def is_palyndrom(string):
    symbols = set(string)
    symbols_dict = {symbol: string.count(symbol) for symbol in symbols}
    count_odd_symbols = 0
    for symbol in symbols_dict:
        if symbols_dict[symbol] % 2 != 0:
            count_odd_symbols += 1
    return count_odd_symbols > 1


if is_palyndrom(string):
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')

