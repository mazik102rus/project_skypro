import pytest

from src.masks import WRONG_DATA_ERR, get_mask_account, get_mask_card_number


@pytest.fixture
def card_data():
    return [
        ('1234567812345678', '1234 56** **** 5678'),
        ('123456781234567', WRONG_DATA_ERR),

    ]


@pytest.fixture
def account_data():
    return [
        ('12345678901234567890', '**7890'),
        ('1234567890', WRONG_DATA_ERR),
    ]


# Тесты для функций


def test_get_mask_card_number(card_data):
    for number, expected in card_data:
        assert get_mask_card_number(number) == expected


def test_get_mask_account(account_data):
    for number, expected in account_data:
        assert get_mask_account(number) == expected
