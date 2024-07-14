from typing import Any
def filter_by_state(input_data: list[dict[str]], state_key = 'EXECUTED') -> list[dict[str]]:
    """Функция фильтрации данных по ключу state"""
    filter_list = []
    for key in input_data:
        if key.get('state') == state_key:
            filter_list.append(key)
        return filter_list


def sort_by_date(input_data: list[dict[str]], reverse=True) -> list[dict[str]]:
    """Функция сортировки исходных данных по дате"""
    return sorted(input_data, key=lambda i: i['date'])
