alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
text = '''Hello
Hello
Hello
Hello'''


def open_write(name, text):
    file_w = open(name, 'w')
    file_w.write(text)
    file_w.close()
    file_r = open(name, 'r')
    return file_r


old_file = open_write('text.txt', text)


def is_upper(symbol, new_str, template, index):
    if symbol.isupper():
        new_str.append(template[index].upper())
    else:
        new_str.append(template[index])


def cezar(file, template):
    max_index = len(template) - 1
    new_text = []
    for index_str, current_str in enumerate(file):
        new_str = []
        for symbol in current_str:
            if symbol == '\n':
                continue
            symbol_index = template.index(symbol.lower())
            new_symbol_index = symbol_index + (index_str + 1)
            if new_symbol_index > max_index:
                right_new_symbol_index = new_symbol_index - max_index
                is_upper(symbol, new_str, template, right_new_symbol_index)
            else:
                is_upper(symbol, new_str, template, new_symbol_index)
        new_text.append(''.join(new_str))
    file.close()
    return '\n'.join(new_text)


new_file = open('cipher_text.txt', 'w')
new_file.write(cezar(old_file, alphabet))
new_file.close()
