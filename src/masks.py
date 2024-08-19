def get_mask_card_number(number_card: str) -> str:
    if number_card == "":
        return "Вы не ввели номер карты"
    if len(number_card) != 16:
        return "Вы ввели не верный номер карты"
    return (f"{number_card[0:4]} {number_card[4:6]}** **** " f"{number_card[-4:]}")


def get_mask_account(number_account: str) -> str:
    if number_account == "":
        return "Вы не ввели номер счета"
    if len(number_account) != 20:
        return "Вы ввели не верный номер счета"
    return (f"**{number_account[-4:]}")


print(get_mask_account("73654108430135874305"))
