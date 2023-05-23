import requests

url = 'https://dummyjson.com/users/{id}'

brown_hair_set = []
louisville_citizens_set = []

for page in range(1, 101):
    response = requests.get(url.format(id=page))
    dummyjson_data = response.json()
    if dummyjson_data['hair']['color'] == 'Brown':
        brown_hair_user_age = dummyjson_data['age']
        brown_hair_set.append(brown_hair_user_age)
    try:
        if dummyjson_data['address']['city'] == 'Louisville':
            louisville_citizen_first_name = dummyjson_data['firstName']
            louisville_citizen_last_name = dummyjson_data['lastName']
            louisville_citizen_full_name = f'{louisville_citizen_first_name} {louisville_citizen_last_name}'
            louisville_citizens_set.append(louisville_citizen_full_name)
    except KeyError:
        pass

brown_hair_set_length = len(brown_hair_set)
brown_hair_set_sum = sum(brown_hair_set)
brown_hair_set_average_age = int(brown_hair_set_sum / brown_hair_set_length)

louisville_citizens = ', '.join(map(str, louisville_citizens_set))

print('Середній вік людей з каштановим волоссям: ', brown_hair_set_average_age)
print('Жителі Louisville:', louisville_citizens)
