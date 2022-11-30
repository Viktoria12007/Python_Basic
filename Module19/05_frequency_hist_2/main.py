text = input('Введите текст: ').lower()


def hystogram(string):
    dictionary = dict()
    for symbol in string:
        if symbol not in dictionary:
            dictionary[symbol] = 1
        else:
            dictionary[symbol] += 1
    return dictionary


dict_symbols = hystogram(text)

print('Оригинальный словарь частот:')
for symbol in sorted(dict_symbols.keys()):
    print(symbol, ':', dict_symbols[symbol])


def get_dict_frequency(dictionary):
    dict_frequency = {item: [symbol for symbol in dictionary if dictionary[symbol] == item]
                      for item in set(dictionary.values())}
    return dict_frequency


dict_frequency = get_dict_frequency(dict_symbols)
print()
print('Инвертированный словарь частот:')
for symbol in dict_frequency:
    print(symbol, ':', dict_frequency[symbol])
