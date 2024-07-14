from typing import Any


def filter_by_state(input_data: list[dict[str, Any]], state_key: str = 'EXECUTED') -> list[dict[str, Any]]:
    """Функция фильтрации данных по ключу state"""
    filter_list = []
    for key in input_data:
        if key.get('state') == state_key:
            filter_list.append(key)
    return filter_list




def sort_by_date(input_data: list[dict[str, Any]], reverse_list: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки исходных данных по дате"""
    sorted_list = sorted(input_data, key=lambda d: d['date'], reverse=reverse_list)
    return sorted_list
