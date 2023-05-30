def makes_comp_list_number(start: int) -> list:
    target_list = [start + number for number in range(10) if start > 1]
    if start < 1:
        raise ValueError
    return target_list


print(makes_comp_list_number(8))
