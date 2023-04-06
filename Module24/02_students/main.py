info_students = [
    {
        'surname_name': 'Голубова Виктория',
        'number_group': 168,
        'progress': [93, 86, 24, 61, 79],
    },
    {
        'surname_name': 'Голубов Владимир',
        'number_group': 44,
        'progress': [38, 74, 24, 27, 70],
    },
    {
        'surname_name': 'Голубов Роман',
        'number_group': 48,
        'progress': [10, 39, 10, 36, 68],
    },
    {
        'surname_name': 'Федорищев Игорь',
        'number_group': 93,
        'progress': [17, 47, 66, 100, 77],
    },
    {
        'surname_name': 'Суранова Анастасия',
        'number_group': 118,
        'progress': [76, 8, 24, 79, 65],
    },
    {
        'surname_name': 'Стрельникова Людмила',
        'number_group': 159,
        'progress': [90, 75, 39, 98, 61],
    },
    {
        'surname_name': 'Стрельников Михаил',
        'number_group': 136,
        'progress': [30, 63, 42, 19, 2],
    },
    {
        'surname_name': 'Стрельников Антон',
        'number_group': 19,
        'progress': [25, 58, 69, 11, 18],
    },
    {
        'surname_name': 'Васильчинко Богдан',
        'number_group': 113,
        'progress': [93, 30, 100, 90, 33],
    },
    {
        'surname_name': 'Кирнос Ирина',
        'number_group': 114,
        'progress': [9, 8, 96, 64, 40],
    },
]


class Student:
    def __init__(self, person):
        self.surname_name = person['surname_name']
        self.number_group = person['number_group']
        self.progress = person['progress']

    def get_middle_progress(self):
        return sum(self.progress) / len(self.progress)

    def display_student(self):
        print(f'Студент {self.surname_name} группы номер {self.number_group} имеет средний бал {self.middle_progress}')


def create_list_students(info_students):
    list_students = []
    for index, person in enumerate(info_students):
        student = Student(person)
        student.middle_progress = student.get_middle_progress()
        list_students.append(student)
    return list_students


def get_sorted_list_students(list_students):
    return sorted(list_students, key=lambda student: student.middle_progress)


def display_list_student(list_students):
    for index, student in enumerate(list_students):
        student.display_student()


list_students = get_sorted_list_students(create_list_students(info_students))
display_list_student(list_students)
