import requests

url = 'https://dummyjson.com/users'

response = requests.get(url)

dummyjson_data = response.json()

clean_data = dummyjson_data['users']

brown_hair_set = []
brown_hair_set_average_age = 0
louisville_citizens_set = []

for user in clean_data:
    if user['hair']['color'] == 'Brown':
        brown_hair_user_age = user['age']
        brown_hair_set.append(brown_hair_user_age)
        brown_hair_set_length = len(brown_hair_set)
        brown_hair_set_sum = sum(brown_hair_set)
        brown_hair_set_average_age = int(brown_hair_set_sum / brown_hair_set_length)
    elif user['address']['city'] == 'Louisville':
        louisville_citizen_first_name = user['firstName']
        louisville_citizen_last_name = user['lastName']
        louisville_citizen_full_name = f'{louisville_citizen_first_name} {louisville_citizen_last_name}'
        louisville_citizens_set.append(louisville_citizen_full_name)

louisville_citizens = ', '.join(map(str, louisville_citizens_set))

print('Середній вік людей з каштановим волоссям: ', brown_hair_set_average_age)
print('Жителі Louisville:', louisville_citizens)
