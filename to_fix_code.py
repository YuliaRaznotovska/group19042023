# очікуваний результат у вигляді: My name is David, I am 14 years old👣

# example
# f = '\N{Footprints}'  # not informative naming, numeric code is better for unicode characters, the correct code below
smile_footprint = '\U0001F463'

# User_ name = input() # names of variables must be lowercase and include no space
# input() must contain a specific call to action text string, the correct code is below
user_name = input('Please, enter your name >>> ')

# User_age =input ('Please, enter your age >>> ')
# names of variables must be lowercase and include space after the equal sign and no space after input
# the correct code is below
user_age = input('Please, enter your age >>> ')

# результат = 'My name is' + User_ name + ", I am" + User_age + 'years old' + smile_footprint
# names of variables must be written in lowercase Latin alphabet with no space
# there must be space after the equal sign
# too many pluses and the quotes must follow one style, the correct code is below
result = f'My name is {user_name}, I am {user_age} years old {smile_footprint}'

# print (результат) # we changed the name of the variable into Latin, no space after print, the correct code below
print(result)
