def open_write(file_name, text):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(text)


def validation(current_str):
    fields = current_str.split(' ')
    if len(fields) != 3:
        raise IndexError('НЕ присутствуют все три поля')
    if not fields[0].isalpha():
        raise NameError('Поле «Имя» содержит НЕ только буквы')
    if '@' not in fields[1] or '.' not in fields[1]:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
    age = int(fields[2])
    if age < 10 or age > 99:
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')


def write_good_bad_registrations(file):
    good_log = []
    bad_log = []
    for current_str in file:
        try:
            without_lit = current_str[:-1]
            validation(without_lit)
        except (IndexError, NameError, SyntaxError, ValueError) as error:
            bad_log.append(f'{without_lit}      {error}')
        else:
            good_log.append(without_lit)
    open_write('registrations_good.log', '\n'.join(good_log))
    open_write('registrations_bad.log', '\n'.join(bad_log))
    file.close()


registrations = open('registrations.txt', 'r', encoding='utf-8')
write_good_bad_registrations(registrations)
