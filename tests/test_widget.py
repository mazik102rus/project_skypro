import pytest

from src.widget import mask_account_card


# Фикстуры для создания необходимых входных данных
@pytest.fixture
def sample_data():
    return [
        (('1234567812345678', 'Maestro'), 'Maestro 1234 56** **** 5678'),
    ]


# Параметризация теста
@pytest.mark.parametrize(
    "input_data,expected_result",
    [
        (('1234567812345678', 'Maestro'), 'Maestro 1234 56** **** 5678'),
        (('9876543210987654', 'Visa Classic'), 'Visa Classic 9876 54** **** 7654'),
        (('4111111111111111', 'Visa Platinum'), 'Visa Platinum 4111 11** **** 1111'),
        (('5500000000000000', 'MasterCard'), 'MasterCard 5500 00** **** 0000'),
    ]
)
def test_mask_account_card(input_data, expected_result):
    number, data_text = input_data
    result = mask_account_card(f"{data_text} {number}")
    assert expected_result == result
