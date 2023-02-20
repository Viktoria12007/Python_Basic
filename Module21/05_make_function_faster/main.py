check_numbers = {}


def calculating_math_func(data, memory):
    result = 1
    if data not in memory:
        start = 1
        if len(memory):
            start += len(memory)
        for index in range(start, data + 1):
            result *= index
            memory[index] = result
    else:
        result = memory[data]
    result /= data ** 3
    result = result ** 10
    return result


print(calculating_math_func(5, check_numbers))
print(calculating_math_func(10, check_numbers))
print(calculating_math_func(12, check_numbers))
