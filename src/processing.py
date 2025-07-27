from datetime import datetime


def filter_by_state(data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Фильтр для списка словарей."""
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: list[dict], descending: bool = True) -> list[dict]:
    """Сортировка по дате."""
    return sorted(
        data,
        key=lambda x: datetime.fromisoformat(x['date']), reverse=descending
    )
