site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}
key = input('Введите искомый ключ: ')
check_max_deep = input('Хотите ввести максимальную глубину? Y/N: ').lower()
max_deep = 1
if check_max_deep == 'y':
    max_deep = int(input('Введите максимальную глубину: '))
answer = None


def search_value_by_key(checked_dict, next_key_item, max_deep):
    if check_max_deep == 'y':
        max_deep -= 1
    level_keys = checked_dict.keys()
    if max_deep > 0 and key not in checked_dict:
        for key_item in level_keys:
            if isinstance(checked_dict[key_item], dict):
                next_key_item = search_value_by_key(checked_dict[key_item], next_key_item, max_deep)
    else:
        if key in checked_dict:
            return checked_dict[key]
        return None
    return next_key_item


print('Значение ключа:', search_value_by_key(site, answer, max_deep))

