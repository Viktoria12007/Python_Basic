text = 'Mama myla ramu.'


def open_write(name, text):
    file_w = open(name, 'w')
    file_w.write(text)
    file_w.close()


def open_write_read(name, text):
    file_w = open(name, 'w')
    file_w.write(text)
    file_w.close()
    file_r = open(name, 'r')
    return file_r


def analys_file(name):
    count_letters = len(tuple(filter(lambda item: item.isalpha(), list(name))))
    symbol_dict = {}
    for index, symbol in enumerate(name):
        if symbol.isalpha():
            if symbol not in symbol_dict:
                symbol_dict[symbol] = 1
            else:
                symbol_dict[symbol] += 1
    for key, value in symbol_dict.items():
        symbol_dict[key] = str(round(value / count_letters, 3))
    return tuple(sorted(sorted(symbol_dict.items(),
                               key=lambda _item: _item[0]), reverse=True, key=lambda item: float(item[1])))


def get_analys_text(sorted_list):
    return '\n'.join(tuple(' '.join(value) for index, value in enumerate(sorted_list)))


text_file = open_write_read('text.txt', text)
open_write('analysis.txt', get_analys_text(analys_file(text_file.read().lower())))
text_file.close()
