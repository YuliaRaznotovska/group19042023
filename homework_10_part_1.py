visited_cities_input = input('Введіть через пробіл міста, в яких Ви побували за останні 10 років >>> ').title()
visited_cities_split = visited_cities_input.split()
visited_cities_set = set(visited_cities_split)

dream_cities_input = input('Введіть через пробіл міста, які Ви бажаете відвідати >>> ').title()
dream_cities_split = dream_cities_input.split()
dream_cities_set = set(dream_cities_split)

cities_common = visited_cities_set.intersection(dream_cities_set)

if cities_common:
    cities_common_message = 'Вам, мабуть дуже сподобалось в містах: ' + ' '.join(cities_common)
    print(cities_common_message)
else:
    print('Ви відкриті до нових пригод')
