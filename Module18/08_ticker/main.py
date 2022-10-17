str_1 = input('Первая строка: ').lower()
str_2 = input('Вторая строка: ').lower()
possibility = False
for letter_index in range(len(str_1)):
    if ''.join([str_1[letter_index:], str_1[:letter_index]]) == str_2:
        possibility = True
        print('Первая строка получается из второй со сдвигом', str(letter_index) + '.')
        break
if not possibility:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
