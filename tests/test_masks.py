from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number('') == ('Вы не ввели номер карты')
    assert get_mask_card_number('7000792200089606361') == 'Проверьте введеные данные карты'

def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account('') == ('Вы не ввели номер счета')
    assert get_mask_account('7000792200089606361') == 'Проверьте введеные данные счета'

