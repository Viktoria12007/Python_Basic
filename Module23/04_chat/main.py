def get_name_user():
    return input('Введите имя пользователя: ')


def choose_action():
    return int(input('''Введите номер выбранного действия:
    1) Посмотреть текущий текст чата.
    2) Отправить сообщение.
    3) Выйти из чата. '''))


def open_read(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    text = file.read()
    file.close()
    return text


def open_write(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        pass


def open_edit(file_name, text):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(text)


def read_chart(file_name):
    text = open_read(file_name)
    if len(text):
        print(text)
    else:
        print('Чат пуст.')


def error_message():
    print('Пожалуйста введите правильный номер действия: 1, 2 или 3')


def chat():
    name = get_name_user()
    while True:
        try:
            action = choose_action()
            if action == 1:
                read_chart('chat.txt')
            elif action == 2:
                message = input('Введите сообщение: ')
                str_chat = f'{name}: {message}\n'
                open_edit('chat.txt', str_chat)
            elif action == 3:
                break
            else:
                error_message()
        except ValueError:
            error_message()
        except FileNotFoundError:
            open_write('chat.txt')
            read_chart('chat.txt')


chat()
