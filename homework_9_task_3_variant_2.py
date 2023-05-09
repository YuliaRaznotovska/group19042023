# Task 3 Variant 2
user_string = str(input('Enter your string >>> '))
user_string.split()
new_user_string = []
result_user_string = []

for user_string_element in user_string:
    if user_string_element.isupper():
        new_user_string.append(user_string_element)
        result_user_string = ''.join(new_user_string)
    else:
        continue
print(result_user_string)
