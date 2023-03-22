def get_reverse_file(name):
    file = open(name, 'r')
    result = ''.join(tuple(line if line.endswith('\n') else line + '\n' for line in file)[::-1])
    file.close()
    return result


print(get_reverse_file('zen.txt'))
