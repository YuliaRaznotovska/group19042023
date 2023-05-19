student = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}

student_update = {
    'Ілон Маск': {
        'Пошта': 'IM@gmail.com',
        'Вік': 31,
        'Номер телефону': '+380682384964',
        'Середній бал': 98
    },
}
student.update(student_update)

total_average_score = 0
students_number = 0
total_average_score_result = 0

for student_name, student_score in student.items():
    average_score = student_score.get('Середній бал')
    if average_score > 90:
        print(f'{student_name} має середній бал {average_score}')
    total_average_score += average_score
    students_number = len(student)
    total_average_score_result = total_average_score / students_number

print('Середній бал групи = ', total_average_score_result)

for student_name in student.values():
    if student_name['Номер телефону'] is None:
        student_name['Номер телефону'] = '+380956498789'
