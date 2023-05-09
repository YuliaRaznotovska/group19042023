my_list = [12, 4, 3.4, 8, 17.6]
new_list = []

for list_element in my_list:
    doubled_list_element = list_element * 2
    new_doubled_list = str(doubled_list_element)
    new_list.append(new_doubled_list)

print(new_list)
