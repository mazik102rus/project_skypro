import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "operationAmount": {
                "currency": {"code": "USD"}
            },
            "description": "Перевод организации"
        },
        {
            "id": 142264268,
            "operationAmount": {
                "currency": {"code": "USD"}
            },
            "description": "Перевод со счета на счет"
        },
        {
            "id": 873106923,
            "operationAmount": {
                "currency": {"code": "RUB"}
            },
            "description": "Перевод со счета на счет"
        }
    ]


# Тесты для filter_by_currency
def test_filter_by_currency(sample_transactions):
    usd_gen = filter_by_currency(sample_transactions, "USD")
    assert next(usd_gen)["id"] == 939719570
    assert next(usd_gen)["id"] == 142264268
    with pytest.raises(StopIteration):
        next(usd_gen)


def test_filter_empty_transactions():
    empty_gen = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(empty_gen)


# Тесты для transaction_descriptions
def test_transaction_descriptions(sample_transactions):
    desc_gen = transaction_descriptions(sample_transactions)
    assert next(desc_gen) == "Перевод организации"
    assert next(desc_gen) == "Перевод со счета на счет"
    assert next(desc_gen) == "Перевод со счета на счет"


def test_descriptions_empty():
    empty_gen = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(empty_gen)


# Тесты для card_number_generator
@pytest.mark.parametrize("start, end, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]),
    (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"])
])
def test_card_number_generator(start, end, expected):
    gen = card_number_generator(start, end)
    assert list(gen) == expected
