my_str = input('Введите строку: ')
current_letter = my_str[0]
count_current_letter = 0
new_str_arr = []
for letter_index in range(len(my_str)):
    if my_str[letter_index] != current_letter:
        new_str_arr.append(''.join([current_letter, str(count_current_letter)]))
        current_letter = my_str[letter_index]
        count_current_letter = 1
    else:
        count_current_letter += 1
    if letter_index == len(my_str) - 1:
        new_str_arr.append(''.join([current_letter, str(count_current_letter)]))
print('Закодированная строка:', ''.join(new_str_arr))
