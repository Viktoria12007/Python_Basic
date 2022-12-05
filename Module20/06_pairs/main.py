import random
original_list = [random.randint(0, 100) for _ in range(10)]
print('Оригинальный список:', original_list)
new_list = [(value, original_list[index + 1]) for index, value in enumerate(original_list)
              if index == 0 or index % 2 == 0]
print('Новый список:', new_list)