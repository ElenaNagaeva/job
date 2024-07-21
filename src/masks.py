
def get_mask_card_number(number_card: str) -> str:
    if len(number_card) != 16 and len(number_card) != 0:
        return "Проверьте введеные данные карты"
    elif number_card == '':
        return "Вы не ввели номер карты"
    elif len(number_card) == 16:
        return (f"{number_card[0:4]} {number_card[4:6]}** **** " f"{number_card[-4:]}")



def get_mask_account(number_account: str) -> str:
    if len(number_account) != 20 and len(number_account) != 0:
        return "Проверьте введеные данные счета"
    elif number_account == '':
        return "Вы не ввели номер счета"
    elif len(number_account) == 20:
        return (f"**{number_account[-4:]}")
