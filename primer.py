#Функция для фильтрации списка словарей по определенному состоянию

def filter_by_state(data, state):
    """Фильтрует список словарей, возвращая только те, которые соответствуют заданному состоянию."""
    filtered_data = []  # Список для хранения отфильтрованных результатов
    for item in data:
        if item.get('state') == state:
            filtered_data.append(item)  # Добавьте элемент, если состояние соответствует
    return filtered_data

# Примеры данных для демонстрации функции
sample_data = [
    {'name': 'Alice', 'state': 'NY'},
    {'name': 'Bob', 'state': 'CA'},
    {'name': 'Charlie', 'state': 'NY'},
    {'name': 'David', 'state': 'TX'}
]

# Пример ввода для функции с определенными значениями
input_data = [
    {'name': 'Eve', 'state': 'FL'},
    {'name': 'Frank', 'state': 'NY'},
    {'name': 'Grace', 'state': 'CA'},
    {'name': 'Hank', 'state': 'NY'},
    {'name': 'Ivy', 'state': 'NY'},
    {'name': 'Jack', 'state': 'TX'}
]

# Filtering by state 'NY'
result = filter_by_state(input_data, 'NY')
print(f"Filtered data for state 'NY': {result}")