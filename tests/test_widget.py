import pytest

from src.widget import mask_account_card


# Фикстуры для создания необходимых входных данных
@pytest.fixture
def sample_data():
    return [
        (('1234567812345678', 'Maestro'), 'Maestro 1234 56** **** 5678')
    ]


def test_mask_account_card(sample_data):
    number, data_text = sample_data[0][0]
    result = mask_account_card(f"{data_text} {number}")
    assert sample_data[0][1] == result
