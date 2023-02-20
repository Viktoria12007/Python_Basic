def get_structure_site(label):
    return {
        'html': {
            'head': {
                'title': f'Куплю/продам {label} недорого'
            },
            'body': {
                'h2': f'У нас самая низкая цена на {label}',
                'div': 'Купить',
                'p': 'продать'
            }
        }
    }


count_sites = int(input('Сколько сайтов: '))
for _ in range(count_sites):
    label = input('Введите название продукта для нового сайта: ')
    print(f'Сайт для {label}:')
    print(f'site = {get_structure_site(label)}')
