# TODO здесь писать код

firstYear = int(input('Введите первый год: '))
secondYear = int(input('Введите второй год: '))

def getBadYears (firstYear, secondYear):
    if len(str(firstYear)) != 4 and len(str(secondYear)) != 4:
        return print('Оба года должны быть четырёхзначными числами!')
    print('Годы от', firstYear, 'до', secondYear, 'с тремя одинаковыми цифрами:')
    for year in range(firstYear, secondYear + 1):
        for simbol in str(year):
            if str(year).count(simbol) == 3:
                print(year)
                break


getBadYears(firstYear, secondYear)
