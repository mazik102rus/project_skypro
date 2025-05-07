def filter_by_state(data, state='EXECUTED'):
    return [item for item in data if item.get('state') == state]

# Пример использования
data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

filtered_data = filter_by_state(data)
print(filtered_data)  # Вывод: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

from datetime import datetime

def sort_by_date(data, descending=True):
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)

sorted_data = sort_by_date(data)
print(sorted_data)