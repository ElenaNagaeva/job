from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_user: str) -> str:
    """Функция маскировки счета/карты"""
    number_spaces = 0
    number_account = 0
    number_card = 0
    for i in input_user:
        if i == " ":
            number_spaces += 1
    if len(input_user.split()[-1]) == 20:
        number_account = get_mask_account(input_user[-20:])
        result = f'{input_user.split()[0]} {number_account}'
    elif number_spaces == 1:
        number_card = get_mask_card_number(input_user[-16:])
        result = f'{input_user.split()[0]} {number_card}'
    elif number_spaces == 2:
        number_card = get_mask_card_number(input_user[-16:])
        result = f'{input_user.split()[0]} {input_user.split()[1]} {number_card}'
    return result



print(mask_account_card("Visa Platinum 8990922113665229"))


def get_data(date_user: str) -> str:
    """Функция преобразования даты в формат дд.мм.гггг"""
    return f'{date_user[8:10]}.{date_user[5:7]}.{date_user[0:4]}'



