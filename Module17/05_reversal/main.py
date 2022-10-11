my_str = input('Введите строку: ').lower()
stop_index = my_str.rfind('h')
start_index = my_str.find('h')
print('Развёрнутая последовательность между первым и последним h:', my_str[start_index + 1:stop_index][::-1])
