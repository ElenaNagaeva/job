from src.widget import mask_account_card, get_data


def test_mask_account_card():
    assert mask_account_card("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"
    assert mask_account_card("Maestro 1596837868705199") == ("Maestro 1596 83** **** 5199")