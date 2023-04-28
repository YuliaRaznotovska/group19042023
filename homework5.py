user_name = input('Please, enter your name >>> ')
user_surname = input('Please, enter your surname >>> ')

translation_map = str.maketrans('', '', '0123456789')
new_user_name = user_name.translate(translation_map).title().strip()
new_user_surname = user_surname.translate(translation_map).upper().strip()
name_length = len(new_user_name)

template = f'Привіт, {new_user_name} {new_user_surname}, а ти знав, що твоє імя складається з {name_length} літер'

replaced_greeting = template.replace('Привіт', 'Здарова')

final_greeting = f'{replaced_greeting}?'

print(final_greeting)
