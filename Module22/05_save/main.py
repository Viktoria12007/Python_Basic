import os

text = input('Введите строку: ')
selected_dir = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ')
name_file = input('Введите имя файла: ')


def open_write_close(path, text):
    file = open(path, 'w')
    file.write(text)
    file.close()


def save_text_in_file(text, selected_dir, name_file):
    path = os.path.join(selected_dir.replace(' ', os.path.sep), name_file)
    if os.path.exists(path):
        is_rewrite = input('Вы действительно хотите перезаписать файл? ').lower()
        if is_rewrite == 'да':
            open_write_close(path, text)
            print('Файл успешно перезаписан!')
    else:
        open_write_close(path, text)
        print('Файл успешно сохранён!')


save_text_in_file(text, selected_dir, name_file)
