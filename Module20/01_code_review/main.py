students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def getInterestsAndLengthAllSurnames(dict_students):
    interests = set()
    surnames = []
    for key, value in dict_students.items():
        interests.update(value['interests'])
        surnames.append(value['surname'])
    surnames_length = len(''.join(surnames))
    return interests, surnames_length


age_students = [(key, value['age']) for key, value in students.items()]

interests, surnames_length = getInterestsAndLengthAllSurnames(students)

print('Список пар "ID студента — возраст":', age_students)
print('Полный список интересов всех студентов:', interests)
print('Общая длина всех фамилий студентов:', surnames_length)
