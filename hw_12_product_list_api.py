import requests

url = 'https://script.google.com/macros/s/AKfycbyVb6YIjJo2N7gXavnLAp614O9PQJtXyL56G7t_QchTh6yy90V9ygHW_FycOXERKGjESw/exec'

response = requests.get(url)

product_data = response.json()

pass

clean_product_data = product_data['data']

product_price_set = []
product_price_gluten_free_set = []
total_price = 0
total_gluten_free_price = 0

for product in clean_product_data:
    product_price = product['product_price']
    product_is_gluten = product['is_gluten']
    product_price_set.append(product_price)
    total_price = sum(product_price_set)
    if product_is_gluten is False:
        product_price_gluten_free_set.append(product_price)
        total_gluten_free_price = sum(product_price_gluten_free_set)

print('Вартість всіх товарів: ', total_price)
print('Вартість всіх товарів без глютена: ', total_gluten_free_price)
