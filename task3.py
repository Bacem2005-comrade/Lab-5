import re
import csv

# Открываем файл
with open('task3.txt', 'r') as file:
    data = file.read()

# Извлекаем данные
ids = re.findall(r'\bd+\b', data)  # ID
surnames = re.findall(r'\b[A-Za-zА-Яа-яЁё]+\b', data)  # Фамилия
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}', data)  # Email
registration_dates = re.findall(r'\bd{1,2}[-/.]d{1,2}[-/.]d{2,4}\b|\bd{4}[-/.]d{1,2}[-/.]d{1,2}\b', data)  # Дата регистрации
websites = re.findall(r'https?://[^s]+', data)  # Сайт

# Сохраняем в CSV
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Фамилия', 'Электронная почта', 'Дата регистрации', 'Сайт'])
    
    for i in range(max(len(ids), len(surnames), len(emails), len(registration_dates), len(websites))):
        writer.writerow([
            ids[i] if i < len(ids) else '',
            surnames[i] if i < len(surnames) else '',
            emails[i] if i < len(emails) else '',
            registration_dates[i] if i < len(registration_dates) else '',
            websites[i] if i < len(websites) else ''
        ])
