count_countries = int(input('Количество стран: '))
countries = {}
for _ in range(count_countries):
    country_info = input(str(_ + 1) + ' страна: ').split()
    countries[country_info[0]] = country_info[1:]
for _ in range(3):
    no_data = True
    city = input(str(_ + 1) + ' город: ')
    for country in countries:
        if city in countries[country]:
            no_data = False
            print('Город', city, 'расположен в стране', country + '.')
            break
    if no_data:
        print('По городу', city, 'данных нет.')
