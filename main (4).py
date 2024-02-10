# # 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова, що складаються не менше ніж з семи літер.
#
# # Відкрий для читання мої записи
# with open('Мої_записи.txt', 'r', encoding='utf-8') as input_file:
#     # Відкрий для записи оброблені мої записи
#     with open('Оброблені_мої_записи.txt', 'w', encoding='utf-8') as output_file:
#         # Команда для читання
#         for line in input_file:
#             # Поділ рядка на слова
#             words = line.split()
#             # Читання кожного слова
#             for word in words:
#                 # Перевірка кажного слова на к-сть із 7 літер
#                 if len(word) >= 7:
#                     # Запис кожного слова у файл оброблені мої записи
#                     output_file.write(word + '\n')


# # 2. Даний текстовий файл. Підрахувати кількість слів у ньому.
#
# # Відкрий для читання мої записи
# with open('Мої_записи.txt', 'r', encoding='utf-8') as file:
#     # Читання файлу
#     content = file.read()
#
# # Текст на слова
# words = content.split()
#
# # Кількість слів
# word_count = len(words)
#
# print(f"Кількість слів у файлі: {word_count}")

# 3. Створіть програму, яка перевіряє текст на неприпустимі слова.

# import re
#
# def load_prohibited_words(file_path):
#     # Створюємо пустий список для заборонених слів
#     prohibited_words = []
#     # Відкриваємо файл зі списком заборонених слів
#     with open(file_path, 'r', encoding='utf-8') as file:
#         # Читаємо кожен рядок у файлі
#         for line in file:
#             # Додаємо слова з кожного рядка у список заборонених слів
#             prohibited_words.append(line.strip())
#     return prohibited_words
#
# def check_for_prohibited_words(text, prohibited_words):
#     replaced_words_count = 0
#     # Розділяємо текст на окремі слова
#     words = re.split(r'([.,:!?])|\s', text)  # Розділяємо текст на слова за пробілами і спецсимволами
#     # Перевіряємо кожне слово у тексті
#     for i in range(len(words)):
#         # Перевіряємо, чи є слово непорожнім рядком і чи є воно в списку заборонених слів
#         if words[i] and words[i].lower() in prohibited_words:
#             words[i] = '*' * len(words[i])  # Замінюємо слово на рядок '*' тієї ж довжини
#             replaced_words_count += 1
#     return replaced_words_count, ' '.join(filter(None, words))
#
# # Завантажуємо список неприпустимих слів з файлу
# prohibited_words = load_prohibited_words('неприпустимі_слова.txt')
#
# # Текст для перевірки
# with open('Мої_записи.txt', 'r', encoding='utf-8') as file:
#     text_to_check = file.read()
#
# # Перевіряємо текст на наявність неприпустимих слів та замінюємо їх
# replaced_count, replaced_text = check_for_prohibited_words(text_to_check, prohibited_words)
#
# # Виводимо статистику
# print(f"Кількість замінених слів: {replaced_count}")
# print("Замінений текст:")
# print(replaced_text)





