def converts_miles_into_km(miles: int | float) -> int | float:
    km = miles * 1.609
    if miles < 0:
        raise ValueError
    return km


def sorts_data(data: str) -> tuple:
    sorted_data = sorted(set(data))
    return tuple(sorted_data)
