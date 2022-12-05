original_list = [6, 3, -1, 8, 4, 10, -5]
stop = False


def is_int(n):
    try:
        return int(n) == float(n)
    except ValueError:
        return -1


def tpl_sort(list):
    for i in range(len(list)):
        for j in range(i, len(list) - 1):
            if list[i] > list[j + 1]:
                list[i], list[j + 1] = list[j + 1], list[i]
    return list


for index, value in enumerate(original_list):
    if not is_int(value):
        stop = True
        break

if stop:
    print(original_list)
else:
    print(tpl_sort(original_list))
