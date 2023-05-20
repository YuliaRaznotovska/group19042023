import requests

url = 'https://script.google.com/macros/s/AKfycbwXfRX9uzPIqkrrxWXHckcUf1t8jlg3_-aHsOspOP93wyzjg289PYplJBMa8iCppaCwiA/exec'

response = requests.get(url)

product_data = response.json()

pass

clean_product_data = product_data['data']

product_price_set = []
product_price_gluten_free_set = []
product_price_sum = 0
gluten_free_price_sum = 0

for product in clean_product_data:
    product_price = product['product_price']
    product_contains_gluten = product['contains_gluten']
    product_stock_number = product['product_stock']
    total_product_price = product_price * product_stock_number
    product_price_set.append(total_product_price)
    product_price_sum = sum(product_price_set)
    if not product_contains_gluten:
        product_price_gluten_free_set.append(total_product_price)
        gluten_free_price_sum = sum(product_price_gluten_free_set)

print('Вартість всіх товарів: ', product_price_sum)
print('Вартість всіх товарів без глютена: ', gluten_free_price_sum)
