

def filter_by_currency(transactions, currency):
    """Генератор, фильтрующий транзакции по заданной валюте"""
    for transaction in transactions:
        operation_currency = transaction["operationAmount"]["currency"]["code"]
        if operation_currency == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Генератор, возвращающий описание транзакций"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    """Генератор номеров банковских карт в заданном диапазоне"""
    for number in range(start, end + 1):
        formatted_number = f"{number:016d}"
        yield " ".join([formatted_number[i:i + 4] for i in range(0, 16, 4)])
