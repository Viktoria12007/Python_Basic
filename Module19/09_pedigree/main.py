count_people = int(input('Введите количество человек: '))
couples = []
tree = dict()
for _ in range(count_people - 1):
    couple_arr = input(str(_ + 1) + ' пара: ').split()
    couple_dict = {'child': couple_arr[0], 'parent': couple_arr[1]}
    couples.append(couple_dict)
father = set(item['parent'] for item in couples) - set(item['child'] for item in couples)
next_father = set()
tree[''.join(list(father))] = 0
order = 0
while len(tree) != count_people:
    order += 1
    for couple in list(filter(lambda x: x['parent'] in father, couples)):
        if couple['child'] not in tree:
            tree[couple['child']] = order
            next_father.add(couple['child'])
    father = set(next_father)
    next_father.clear()
print('«Высота» каждого члена семьи:')
for member in sorted(list(tree)):
    print(member, tree[member])
