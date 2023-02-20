nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
flat_list = []

def get_flat_list(nested_list):
    for index, element in enumerate(nested_list):
        if isinstance(element, list):
            get_flat_list(element)
        else:
            flat_list.append(element)
    return flat_list


print('Ответ:', get_flat_list(nice_list))
