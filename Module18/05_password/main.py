while True:
    password = input('Придумайте пароль: ')
    count_numbers = 0
    for current_simbol in password:
        if current_simbol.isnumeric():
            count_numbers += 1
    if len(password) < 8 or password.islower() or count_numbers < 3:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
