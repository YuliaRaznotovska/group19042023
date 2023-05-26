def turn_number_into_joke(number: int) -> str:
    """Task 1"""
    joke_school = 'What does your computer do for lunch? Has a byte!'
    joke_fisherman = 'Him: Nice fish, where did you catch him? Me:In the water! Him:What did you catch him on? Me: ' \
                     'Experience!'
    joke_cat = 'What\'s it called when all the treats are gone? A cat-astrophe.'
    if number == 1:
        return joke_school
    if number == 2:
        return joke_fisherman
    else:
        return joke_cat


print(turn_number_into_joke(1))
print(turn_number_into_joke(2))
print(turn_number_into_joke(88))


def rectangle_perimeter(width, length) -> float:
    """Task 2"""
    perimeter_result = (width + length) * 2
    return perimeter_result


print(rectangle_perimeter(24, 3))


def deletes_letters_in_string(input_word: str) -> str:
    """Task 3"""
    for letter in input_word:
        if letter.lower() in ('ї', 'ж'):
            input_word = input_word.replace(letter, '')
    return input_word


def deletes_common_letters(original_word: str, word_to_compare: str) -> str:
    original_word = original_word.lower()
    word_to_compare = word_to_compare.lower()
    for letters in word_to_compare:
        if letters in original_word:
            original_word = original_word.replace(letters, '')
    return original_word


print(deletes_letters_in_string('Їжак'))
print(deletes_common_letters('хижак', 'вікно'))
print(deletes_common_letters('вОно', 'вікно'))
