from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_user: str) -> str:
    """Функция маскировки счета/карты"""
    number_spaces = 0
    for i in input_user:
        if i == " ":
            number_spaces += 1
    if len(input_user.split()[-1]) == 20:
        namber_account = get_mask_account(input_user)
        result = f'{input_user.split()[0]} {namber_account}'
    elif number_spaces == 5:
        namber_card = get_mask_card_number(input_user[-19:])
        result = f'{input_user.split()[0]} {input_user.split()[1]} {namber_card}'
    elif number_spaces == 4:
        namber_card = get_mask_card_number(input_user[-19:])
        result = f'{input_user.split()[0]} {namber_card}'

    return result


print(mask_account_card(input()))


def get_data(date_user: str) -> str:
    """Функция преобразования даты в формат дд.мм.гггг"""
    return f'{date_user[8:10]}.{date_user[5:7]}.{date_user[0:4]}'


print(get_data(input()))
