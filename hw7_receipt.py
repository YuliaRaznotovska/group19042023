import textwrap
from datetime import datetime
from decimal import Decimal

# goods 1 section
item_1_title = textwrap.shorten(input('Введіть назву першого товару: ').ljust(20, '.'), width=20, placeholder='...')
item_1_quantity = input('Введіть бажаєму кількість першого товару (цілі одиниці, як 1, 2, 10): ')
item_1_cost_input = Decimal(input('Введіть ціну першого товару (наприклад: 10, 10.50): '))
item_1_cost = item_1_cost_input.quantize(Decimal('1.00'))

# goods 2 section
item_2_title = textwrap.shorten(input('Введіть назву другого товару: ').ljust(20, '.'), width=20, placeholder='...')
item_2_quantity = input('Введіть бажаєму кількість другого товару (цілі одиниці, як 1, 2, 10): ')
item_2_cost_input = Decimal(input('Введіть ціну другого товару (наприклад: 10, 10.50): '))
item_2_cost = item_2_cost_input.quantize(Decimal('1.00'))

item_1_total_cost = Decimal(item_1_quantity) * Decimal(item_1_cost)
item_1_total_cost_right_format = item_1_total_cost.quantize(Decimal('1.00'))

item_2_total_cost = Decimal(item_2_quantity) * Decimal(item_2_cost)
item_2_total_cost_right_format = item_2_total_cost.quantize(Decimal('1.00'))

product_quantity = int(item_1_quantity) + int(item_2_quantity)

product_total_cost = Decimal(item_1_total_cost_right_format) + Decimal(item_2_total_cost_right_format)

printing_template = '{}\t\t\t\t\t{}\t\t\t\t{}\t\t\t{}'

# printing receipt
print('\n\n\n')
print('фіскальний чек'.capitalize().center(80, '~'))
print('магазин "все для дому"'.upper().center(80))
print(f'Товар\t\t\t\t\t\t\t\t\tкількість\t\tціна\t\tвартість')
print(printing_template.format(item_1_title, item_1_quantity, item_1_cost, item_1_total_cost_right_format))
print(printing_template.format(item_2_title, item_2_quantity, item_2_cost, item_2_total_cost_right_format))
print('~' * 80)
print(printing_template.format(
    'ВСЬОГО'.ljust(20),
    product_quantity,
    'x',
    product_total_cost.quantize(Decimal('1.00'))
)
)
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S').rjust(80))
print('\n\n')
