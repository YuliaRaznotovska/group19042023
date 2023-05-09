students_surname = input('Enter your surname separated by spaces >>> ').title()
students_list = students_surname.split()
students_list.sort()

for students in students_list:
    if students.isalpha():
        print(students)
    else:
        print(students + ' is not a surname')
