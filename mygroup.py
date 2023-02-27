groupmates = [
    {
        "name": "Александр",
        "surname": "Беловитский",
        "exams": ["Философия", "ВВИТ", "АиГ"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Игорь",
        "surname": "Скоморохов",
        "exams": ["Философия", "ВВИТ", "АиГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Тимофей",
        "surname": "Горохов",
        "exams": ["Философия", "ВВИТ", "АиГ"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Мария",
        "surname": "Смирнова",
        "exams": ["Философия", "ВВИТ", "АиГ"],
        "marks": [4, 4, 5]
    },
    {
        "name": "Кирилл",
        "surname": "Кварацхелия",
        "exams": ["Философия", "ВВИТ", "АиГ"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Екатерина",
        "surname": "Бацких",
        "exams": ["Философия", "ВВИТ", "АиГ"],
        "marks": [4, 5, 3]
    }
]


def average_mark(gpa_input):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for i in groupmates:
        sum_marks = 0  # сумма оценок
        count_marks = 0  # количество оценок
        for k in i["marks"]:
            count_marks += 1
            sum_marks += k
        gpa_mate = sum_marks / count_marks  # средний балл
        if float(gpa_input) < gpa_mate:
            print(i["name"].ljust(15), i["surname"].ljust(10), str(i["exams"]).ljust(30), str(i["marks"]).ljust(20))


average_mark(input())
