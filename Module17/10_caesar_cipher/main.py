alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
            'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'Ъ', 'ы', 'ь', 'э', 'ю', 'я']
message = input('Введите сообщение: ').lower()
shift = int(input('Введите сдвиг: '))


def get_encrypted_message(message):
    encrypted_message = []
    for letter in message:
        if letter != " ":
            old_index = alphabet.index(letter)
            new_index = old_index + shift
            if new_index >= len(alphabet):
                new_index = new_index - len(alphabet)
            encrypted_message.append(alphabet[new_index])
        else:
            encrypted_message.append(letter)
    return "".join(encrypted_message)

print('Зашифрованное сообщение:', get_encrypted_message(message))
