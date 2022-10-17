name_file = input('Название файла: ')
if name_file.startswith(('@', '№', '$', '%', '^', '&', '\\', '*', '(', ')')):
    print('Ошибка: название начинается на один из специальных символов.')
if not name_file.endswith(('.txt', '.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
if not name_file.startswith(('@', '№', '$', '%', '^', '&', '\\', '*', '(', ')')) \
        and name_file.endswith(('.txt', '.docx')):
    print('Файл назван верно.')
