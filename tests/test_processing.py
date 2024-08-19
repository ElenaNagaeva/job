from src.masks import filter_by_state, sort_by_date


def test_filter_by_state():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("") == "Вы не ввели номер карты"
    assert get_mask_card_number("700792289606361") == "Вы ввели не верный номер карты"
