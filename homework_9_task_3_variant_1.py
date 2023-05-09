# Task 3 Variant 1
user_string = str(input('Enter your string >>> '))
new_user_string = []
new_user_string_length = len(new_user_string)

for user_string_element in user_string:
    if user_string_element.isupper():
        new_user_string.append(user_string_element)
print(*new_user_string, sep='')
