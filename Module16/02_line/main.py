first_class = []
second_class = []
for height in range(160, 176 + 1, 2):
    first_class.append(height)
for height in range(162, 180 + 1, 3):
    second_class.append(height)
first_class.extend(second_class)


def sort_class_by_height(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[i] > unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    return unsorted_list


sorted_list = sort_class_by_height(first_class)
print('Отсортированный список учеников:', sorted_list)
