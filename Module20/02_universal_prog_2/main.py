def is_prime(iterable_object):
    n = len(iterable_object)
    a = [x for x in range(n + 1)]
    a[1] = 0
    primes_list = []

    i = 2
    while i <= n:
        if a[i] != 0:
            primes_list.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    return primes_list


def crypto(iterable_object):
    primes_list = is_prime(iterable_object)
    return [item for index, item in enumerate(iterable_object) if index in primes_list]


string = 'О Дивный Новый мир!'
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
dictionary = {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
        }
print(crypto(dictionary))
