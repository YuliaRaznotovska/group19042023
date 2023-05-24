def turn_number_into_joke(number) -> str:
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


def deletes_letters_in_string(word1: str, word2: str, word3: str):
    """Task 3"""
    disallowed_letters = 'їж'
    for letter in disallowed_letters:
        word1 = word1.replace(letter, '')
    word2 = word2.lower()
    word3 = word3.lower()
    for letters in word3:
        if letters in word2:
            word2 = word2.replace(letters, '')
    return word1, word2


print(deletes_letters_in_string("їжак", 'хижак', 'вікно'))
print(deletes_letters_in_string("їжак", 'вОно', 'вікно'))
