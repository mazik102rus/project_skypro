import pytest
from src.processing import filter_by_state, sort_by_date


# Фикстуры для создания необходимых входных данных
@pytest.fixture
def sample_data():
    return [
        {'date': '2023-01-01T12:00:00', 'state': 'EXECUTED'},
        {'date': '2023-01-02T12:00:00', 'state': 'CANCELLED'},
        {'date': '2023-01-03T12:00:00', 'state': 'EXECUTED'},
    ]


# Параметризация для теста фильтрации
@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELLED", 1),
        ("PENDING", 0),  # Тестирование несуществующего состояния
    ]
)
def test_filter_by_state(sample_data, state, expected_count):
    filtered = filter_by_state(sample_data, state)
    assert len(filtered) == expected_count


# Параметризация для теста сортировки
@pytest.mark.parametrize(
    "descending, expected_first_date",
    [
        (True, '2023-01-03T12:00:00'),  # По убыванию
        (False, '2023-01-01T12:00:00')   # По возрастанию
    ]
)
def test_sort_by_date(sample_data, descending, expected_first_date):
    sorted_data = sort_by_date(sample_data, descending=descending)
    assert sorted_data[0]['date'] == expected_first_date
