count_couples = int(input('Введите количество пар слов: '))
dictionary = dict()
for _ in range(count_couples):
    couples = input(str(_ + 1) +' пара, слова вводите через пробел: ').lower()
    dictionary[_] = couples.split()
flag = True
while flag:
    word = input('Введите слово: ').lower()
    for keys in dictionary:
        if word in dictionary[keys]:
            print('Синоним:', ''.join(list(filter(lambda x: x != word, dictionary[keys]))))
            flag = False
    if flag:
        print('Такого слова в словаре нет.')
