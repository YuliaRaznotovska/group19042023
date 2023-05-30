def gen_month():
    months_list = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    ]
    while True:
        for month in months_list:
            yield month


gen = gen_month()

for i in gen_month():
    print(next(gen))
