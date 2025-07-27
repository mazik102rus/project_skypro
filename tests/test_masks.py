import pytest

from src.masks import WRONG_DATA_ERR, get_mask_account, get_mask_card_number


# Фикстуры для создания необходимых входных данных
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


# Добавляем параметризацию для теста карты
@pytest.mark.parametrize("number,expected", [
    ('1234567812345678', '1234 56** **** 5678'),
    ('123456781234567', WRONG_DATA_ERR),
])
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


# Добавляем параметризацию для теста счета
@pytest.mark.parametrize("number,expected", [
    ('12345678901234567890', '**7890'),
    ('1234567890', WRONG_DATA_ERR),
])
def test_get_mask_account(number, expected):
    assert get_mask_account(number) == expected
