from masks import get_mask_account, get_mask_card_number


def mask_account_card(input_user: str) -> str:
    if len(input_user.split()[-1]) == 20:
        namber_account = get_mask_account(input_user)
        result = f'{input_user.split()[0]} {namber_account}'
    elif (input_user.split()[0]) == "Maestro":
        namber_card = get_mask_card_number(input_user[-16:])
        result = f'{input_user.split()[0]} {namber_card}'
    elif (input_user.split()[0]) == "Visa":
        namber_card = get_mask_card_number(input_user[-16:])
        result = f'{input_user.split()[0]} {input_user.split()[1]} {namber_card}'

    return print(result)


mask_account_card(input())


def get_data(date_user: str) -> str:
    return print(f'{date_user[8:10]}.{date_user[5:7]}.{date_user[0:4]}')


get_data(input())
