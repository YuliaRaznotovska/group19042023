def decorator_checks_output_value_type(func):
    def wrapper(value):
        dec_result = func(value)
        if type(dec_result) == str:
            dec_result_formatted = f'<b>{dec_result}</b>'
            return dec_result_formatted
        else:
            return dec_result
    return wrapper


@decorator_checks_output_value_type
def some_func(value) -> str:
    result = value
    return result


print(some_func('dddd'))


def decorator_checks_output_value_type_version_2(func):
    def wrapper(value):
        dec_result = func(value)
        if type(dec_result) == str:
            dec_result_formatted = f'\033[1m{dec_result}'
            return dec_result_formatted
        else:
            return dec_result
    return wrapper


@decorator_checks_output_value_type_version_2
def some_func2(value) -> str:
    result = value
    return result


print(some_func2('dddd'))
