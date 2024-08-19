from typing import Any


def filter_by_state(input_data: list[dict[str, Any]], state_key: str = 'EXECUTED') -> list[dict[str, Any]]:
    """Функция фильтрации данных по ключу state"""
    filter_list = []
    for key in input_data:
        if key.get('state') == state_key:
            filter_list.append(key)
    if filter_list == []:
        return "данных, удовлетворяющих условию, нет"
    return filter_list


def sort_by_date(input_data: list[dict[str, Any]], reverse_list: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки исходных данных по дате"""
    sorted_list = sorted(input_data, key=lambda d: d['date'], reverse=reverse_list)
    return sorted_list


print(filter_by_state([{'id': 41428829, 'state': 'EXETED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))