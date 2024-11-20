import re

# Открываем файл
with open('task1-en.txt', 'r') as file:
    text = file.read()

# Находим все слова, начинающиеся с большой буквы
capitalized_words = re.findall(r'\b[A-ZА-ЯЁ][a-zа-яё]*\b', text)

print("Слова, начинающиеся с большой буквы:", capitalized_words)




