message = input('Сообщение: ').split()
punctuation_marks = [',', '.', '?', '!', ':', ';']
final_text = []
for word in message:
    if word.isalpha():
        final_text.append(word[::-1])
    else:
        broken_word = [f' {word[letter_index]} ' if not word[letter_index].isalpha()
                       else word[letter_index] for letter_index in range(len(word))]
        broken_word = ''.join(broken_word)
        broken_word = broken_word.split()
        reversed_word = ''.join([broken_word[letter_index][::-1] if broken_word[letter_index].isalpha()
                         else broken_word[letter_index] for letter_index in range(len(broken_word))])
        final_text.append(reversed_word)
print('Новое сообщение:', ' '.join(final_text))
