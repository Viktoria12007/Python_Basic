def get_sum(name_file):
    numbers_file = open(name_file, 'r')
    count = 0
    for line in numbers_file:
        without_space = line.strip()
        if without_space.isnumeric():
            count += int(without_space)
    numbers_file.close()
    return str(count)


sum_file = open('answer.txt', 'w')
sum_file.write(get_sum('numbers.txt'))
sum_file.close()
