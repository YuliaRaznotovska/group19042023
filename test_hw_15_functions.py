import hw_15_functions


def test_converts_miles_into_km_value_int():
    miles = 3
    assert type(hw_15_functions.converts_miles_into_km(miles)) in (int, float)


def test_converts_miles_into_km_value_float():
    miles = 3.5
    assert type(hw_15_functions.converts_miles_into_km(miles)) in (int, float)


def test_converts_miles_into_km_value_zero():
    miles = 0
    assert type(hw_15_functions.converts_miles_into_km(miles)) in (int, float)


def test_converts_miles_into_km_value_negative():
    miles = -3
    try:
        hw_15_functions.converts_miles_into_km(miles)
        assert False
    except ValueError:
        assert True


def test_converts_miles_into_km_value_string():
    miles = '3'
    try:
        hw_15_functions.converts_miles_into_km(miles)
        assert False
    except TypeError:
        assert True


def test_sorts_data_input_value_int():
    data = 125
    try:
        hw_15_functions.sorts_data(data)
        assert False
    except TypeError:
        assert True


def test_sorts_data_input_value_str():
    data = 'abcdefg'
    hw_15_functions.sorts_data(data)
    assert True


def test_sorts_data_output_value_type():
    data = 'abcd'
    assert type(hw_15_functions.sorts_data(data)) == tuple


def test_sorts_data_input_value_type():
    data = 9378
    try:
        sorted_tuple = sorted(hw_15_functions.sorts_data(data))
        assert type(sorted_tuple) == str
    except TypeError:
        pass


def test_sorts_data_input_value_zero():
    data = 0
    try:
        hw_15_functions.sorts_data(data)
        assert False
    except TypeError:
        assert True
