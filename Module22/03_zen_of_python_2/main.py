import os


def open_file(name):
    file = open(os.path.abspath(os.path.join('..', '02_zen_of_python', name)), 'r')
    data = file.read()
    return file, data


def close_file(name):
    name.close()


def get_count_letters(data):
    count = 0
    for letter in data:
        if letter.isalpha():
            count += 1
    return count


def get_count_words(data):
    data_without_spaces = data.split()
    count = 0
    for index, word in enumerate(data_without_spaces):
        for letter in word:
            if letter.isalpha():
                count += 1
                break
    return count


def get_count_lines(data):
    return data.count('\n') + 1


def get_count_rarest_letters(data):
    all_isalpha_symbols = tuple(symbol.lower() for symbol in data if symbol.isalpha())
    symbols = {}
    for index, symbol in enumerate(all_isalpha_symbols):
        if symbol not in symbols:
            symbols[symbol] = 1
        else:
            symbols[symbol] += 1

    return sorted(symbols.items(), key=lambda item: item[1])[0][0]


file, data = open_file('zen.txt')
print('Количество букв в файле:', get_count_letters(data))
print('Количество слов в файле:', get_count_words(data))
print('Количество строк в файле:', get_count_lines(data))
print('Наиболее редкая буква:', get_count_rarest_letters(data))
close_file(file)
