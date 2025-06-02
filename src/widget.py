"""Модуль виджетов."""

from datetime import datetime

from src.masks import DEFAULT_DIVIDER, get_mask_account, get_mask_card_number

ACCOUNT_DATA_TYPES = ["Счет", "Счёт", "счет", "счёт"]
CARD_DATA_TYPES = ["Maestro", "MasterCard", "Visa Classic", "Visa Platinum", "Visa Gold"]
DATA_TYPES = ["account", "card"]
UNKNOWN_DATA_ERR = "Ошибка. Данные не распознаны."
DATE_INPUT_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
DATE_OUTPUT_FORMAT = "%d.%m.%Y"


def check_data_type(data_text: str) -> str:
    """Проверка типа переданных данных."""
    if data_text in ACCOUNT_DATA_TYPES:
        return DATA_TYPES[0]
    elif data_text in CARD_DATA_TYPES:
        return DATA_TYPES[1]
    return UNKNOWN_DATA_ERR


def split_data(data: str, divider: str = DEFAULT_DIVIDER) -> tuple:
    """Функция для разделения текста и номера."""
    data_list = data.split(divider)
    number = data_list.pop(-1)
    data_type = divider.join(data_list)
    return number, data_type


def mask_account_card(data: str) -> str:
    """Функция для маскировки номера счета или карты."""
    number, data_text = split_data(data)
    data_type = check_data_type(data_text)
    if data_type == DATA_TYPES[0]:
        return DEFAULT_DIVIDER.join((data_text, get_mask_account(number)))
    elif data_type == DATA_TYPES[1]:
        return DEFAULT_DIVIDER.join((data_text, get_mask_card_number(number)))
    return data_type


def get_date(date: str) -> str:
    """Функция для смены формата даты."""
    return datetime.strptime(date, DATE_INPUT_FORMAT).strftime(DATE_OUTPUT_FORMAT)


if __name__ == "__main__":
    dataset = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
        "Счет номер 73654108430135874305",
        "Счёт 123",
        "Mastercard 7158300734726758",
    ]
    [print(mask_account_card(data)) for data in dataset]
    dates_dataset = [
        "2024-03-11T02:26:18.671407",
        "2024-04-11T15:26:18.671407",
        "2024-03-22T02:50:18.671407",
        "2014-03-11T02:26:33.671407",
        "2025-12-11T02:26:18.123107",
    ]
    [print(get_date(data)) for data in dates_dataset]
