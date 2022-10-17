my_str = input('Введите строку: ')
my_str_arr = my_str.split()
max_len_str = ''
for index_str in range(len(my_str_arr)):
    if len(my_str_arr[index_str]) > len(max_len_str):
        max_len_str = my_str_arr[index_str]
print('Самое длинное слово:', max_len_str)
print('Длина этого слова:', len(max_len_str))
