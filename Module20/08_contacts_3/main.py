contacts = {}


def add_contact():
    name_surname = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
    if name_surname in contacts.keys():
        print('Такой человек уже есть в контактах.')
    else:
        tel = int(input('Введите номер телефона: '))
        contacts.update({name_surname: tel})
    print('Текущий словарь контактов:', contacts)


def search_contacts():
    surname = input('Введите фамилию для поиска: ').lower()
    for key, value in contacts.items():
        if key[1].lower() == surname:
            print(' '.join(key), value)


while True:
    action = int(input('''Введите номер действия:
    1. Добавить контакт
    2. Найти человека
    '''))
    if action == 1:
        add_contact()
    elif action == 2:
        search_contacts()
    else:
        print('Пожалуйста, введите 1 или 2')

