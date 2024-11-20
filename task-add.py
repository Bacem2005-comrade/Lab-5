import re

# Открываем файл
with open('task_add.txt', 'r') as file:
    noise_data = file.read()

# Находим даты (разные форматы)
dates = re.findall(r'\bd{1,2}[-/.]d{1,2}[-/.]d{2,4}\b|\bd{4}[-/.]d{1,2}[-/.]d{1,2}\b', noise_data)

# Находим адреса электронной почты
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}', noise_data)

# Находим адреса сайтов
websites = re.findall(r'https?://[^s]+', noise_data)

# Выводим результаты
print("Найденные даты:", dates)
print("Найденные адреса электронной почты:", emails)
print("Найденные адреса сайтов:", websites)
