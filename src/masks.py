
def get_mask_card_number(number_card: str) -> str:
    return (f"{number_card[0:4]} {number_card[5:7]}** **** " f"{number_card[-4:]}")


def get_mask_account(number_account: str) -> str:
    return (f"**{number_account[-5:-1]}")



