from collections import Counter


def can_be_poly(my_str: str) -> bool:
    c = Counter(my_str).most_common()
    count_even_elements = len(list(filter(lambda item: item[1] % 2 == 0, c)))
    count_odd_elements = len(c) - count_even_elements
    if (count_even_elements >= 1 and count_odd_elements <= 1) or (count_even_elements == 0 and count_odd_elements == 1)\
            or (count_even_elements >= 1 and count_odd_elements == 0):
        return True
    return False


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
print(can_be_poly('bbb'))
print(can_be_poly('aabb'))
print(can_be_poly('bbbc'))
