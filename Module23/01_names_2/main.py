def open_write(file_name, text):
    with open(file_name, 'w', encoding='utf-8') as file_w:
        file_w.write(text)
        return file_name


def get_count_symbols(file_name):
    with open(file_name, 'r', encoding='utf-8') as file_r:
        all_letters = 0
        errors = []
        for index, current_str in enumerate(file_r):
            try:
                count_letters = len(tuple(filter(lambda x: x.isalpha(), list(current_str))))
                all_letters += count_letters
                if count_letters < 3:
                    raise ValueError
            except ValueError:
                text_error = f'Ошибка: менее трёх символов в строке {index}.\n'
                errors.append(text_error)
                print(text_error[:-1])
        open_write('errors.log', ''.join(errors))
        return all_letters


text = 'Василий\nНиколай\nНадежда\nНикита\nЯн\nОльга\nЕвгения\nКристина'


print('Общее количество символов:', get_count_symbols(open_write('people.txt', text)))
