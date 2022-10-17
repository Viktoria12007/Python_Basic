IP_address = input('Введите IP: ')
count = 0
flag = True
while count < 1:
    count += 1
    if IP_address.count('.') != 3:
        print('Адрес — это четыре числа, разделённые точками.')
        break
    IP_address_arr = IP_address.split('.')
    for number in IP_address_arr:
        if not number.isdigit():
            print(number, '— это не целое число.')
            flag = False
            break
        if int(number) > 255:
            print(number, 'превышает 255.')
            flag = False
            break
    if not flag:
        break
else:
    print('IP-адрес корректен.')
