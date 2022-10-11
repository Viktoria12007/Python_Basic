text = input('Введите текст: ')
vowels = ['а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е']
total_vowels = [letter for letter in text.lower() if letter in vowels]
print('Список гласных букв:', total_vowels)
print('Длина списка:', len(total_vowels))
