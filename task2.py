import re

# Открываем файл task2.html
filename = 'task2.html'

try:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # Находим все закрывающие теги
    closing_tags = re.findall(r'</([a-zA-Z0-9]+)>', text)

    # Удаляем повторения, преобразуя в множество
    unique_closing_tags = set(closing_tags)

    # Преобразуем множество обратно в список и сортируем
    sorted_unique_closing_tags = sorted(unique_closing_tags)

    # Выводим результаты
    print("Уникальные закрывающие теги:")
    for tag in sorted_unique_closing_tags:
        print(tag)

except FileNotFoundError:
    print(f"Файл '{filename}' не найден. Пожалуйста, убедитесь, что он существует в текущем каталоге.")
except UnicodeDecodeError:
    print(f"Ошибка декодирования файла '{filename}'. Попробуйте использовать другую кодировку.")

