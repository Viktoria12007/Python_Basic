a = [{"x": 4}, "b", "z", "d"]
b = (10, {20}, [30], "z")

# a = [1, 2, 3, 4, 5]
# b = {1: "s", 2: "q", 3: 4}
# x = (1, 2, 3, 4, 5)


def check_length(*args):
    return len(min(*args, key=len))


min_len = check_length(a, b)

final_arr = []


def my_zip(*args, stop=0):
    if stop <= min_len - 1:
        final_arr.append(tuple(arg[stop] if not isinstance(arg, dict) else list(arg.keys())[stop]
                               for index, arg in enumerate(args)))
        my_zip(*args, stop=stop + 1)
    return final_arr


print(my_zip(a, b))
# print(my_zip(a, b, x))
