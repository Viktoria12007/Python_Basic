from collections import Counter


def can_be_poly(my_str: str) -> bool:
    return len(list(filter(lambda count: count % 2, Counter(my_str).values()))) <= 1


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
print(can_be_poly('bbb'))
print(can_be_poly('aabb'))
print(can_be_poly('bbbc'))
