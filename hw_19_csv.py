import csv

with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, fieldnames=['ident', 'type', 'name', 'elevation_ft', 'continent', 'iso_country'],
                            delimiter=';')
    for airport in list(reader)[1:]:
        if airport['iso_country'] == 'UA':
            print(airport['name'])
