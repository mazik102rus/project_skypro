CARD_NUMBER_LEN = 16
ACCOUNT_NUMBER_LEN = 20
CODED_CHAR = "*"
CARD_NUMBER_HIDE_SYMBOLS = [6, 11]
ACCOUNT_NUMBER_HIDE_SYMBOLS = [0, 1]
ACCOUNT_MASK_LEN = 6
CARD_NUMBER_SUBSTR_LEN = 4
WRONG_DATA_ERR = "Проверьте вводимые данные."
DEFAULT_DIVIDER = " "


def check_number(data: str, len_expected: int) -> bool:
    """Функция проверки входных данных."""
    return data.isnumeric() and len(data) == len_expected


def hide_symbols(data: str, first_index: int, last_index: int) -> str:
    """Функция скрытия символов строки в указанном диапазоне."""
    data = "".join(
        [(CODED_CHAR if first_index <= char_id <= last_index else data[char_id]) for char_id in range(len(data))]
    )
    return data


def add_spaces(data: str, substr_len: int, divider: str = DEFAULT_DIVIDER) -> str:
    """Функция для разбиения строки на блоки."""
    return divider.join([data[char_id : char_id + substr_len] for char_id in range(0, len(data), substr_len)])


def get_mask_card_number(data: str) -> str:
    """Функция для генерации маски номера карты."""
    if check_number(data, CARD_NUMBER_LEN):
        data = hide_symbols(data, *CARD_NUMBER_HIDE_SYMBOLS)
        data = add_spaces(data, CARD_NUMBER_SUBSTR_LEN)
        return data
    else:
        return WRONG_DATA_ERR


def get_mask_account(data: str) -> str:
    """Функция для генерации маски номера карты."""
    if check_number(data, ACCOUNT_NUMBER_LEN):
        data = data[len(data) - ACCOUNT_MASK_LEN : len(data)]
        data = hide_symbols(data, *ACCOUNT_NUMBER_HIDE_SYMBOLS)
        return data
    else:
        return WRONG_DATA_ERR
