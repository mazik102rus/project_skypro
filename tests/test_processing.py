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


def test_filter_by_state(sample_data):
    executed = filter_by_state(sample_data, 'EXECUTED')
    assert len(executed) == 2


def test_sort_by_date(sample_data):
    sorted_data = sort_by_date(sample_data, descending=True)
    assert sorted_data[0]['date'] == '2023-01-03T12:00:00'
    assert sorted_data[1]['date'] == '2023-01-02T12:00:00'
    assert sorted_data[2]['date'] == '2023-01-01T12:00:00'
