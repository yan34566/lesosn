import random

random_numbers = [random.randint(-100, 100) for _ in range(23)]
print(random_numbers)
sum_negative = sum(x for x in random_numbers if x < 0)
print("сума негативних чисел:", sum_negative)
sum_even = sum(x for x in random_numbers if x % 2 == 0)
print("сума парних чисел:", sum_even)
sum_odd = sum(x for x in random_numbers if x % 2 != 0)
print("сума непарных чисел:", sum_odd)
product_index_3 = 1
for i in range(0, len(random_numbers), 3):
        product_index_3*= random_numbers[i]
print("добуток цифр з кратніми індеском 3:", product_index_3)
min_index = random_numbers.index(min(random_numbers))
max_index = random_numbers.index(max(random_numbers))
product_between_min_max = 1
for i in range(min_index+1, max_index):
        product_between_min_max*= random_numbers[i]
print("добуток елментів між максимальни  та мінімальним значеням:", product_between_min_max)
positive_index = [ i for i, x in enumerate(random_numbers) if x > 0]
if len(positive_index) >= 2:
    first_positive_index, last_positive_index = positive_index[0], positive_index[-1]
    sum_between_posetives = sum(random_numbers[first_positive_index +1:last_positive_index])
    print("сума між остані та першим позитивним елементом:", sum_between_posetives)
else:
    print("помлка в списку")

# Генерація випадкового списку цілих чисел (перший список)
random_numbers = [random.randint(-50, 50) for _ in range(10)]

# ■ Створити список цілих, що містить лише парні числа з першого списку;
even_numbers = [num for num in random_numbers if num % 2 == 0]

# ■ Створити список цілих, що містить лише непарні числа з першого списку;
odd_numbers = [num for num in random_numbers if num % 2 != 0]

# творити список цілих, що містить лише негативні числа з першого списку;
negative_numbers = [num for num in random_numbers if num < 0]

# ■ Створити список цілих, що містить лише позитивні числа з першого списку.
positive_numbers = [num for num in random_numbers if num > 0]

# Результат в консоль
print("Початковий список:" , random_numbers)
print("Парні числа:", even_numbers)
print("Непарні числа:", odd_numbers)
print("Негативні числа:", negative_numbers)
print("Позитивні числа:", positive_numbers)

#Додаткові завдання:

# створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99 від 10 до 99
matrix = [[random.randint(10, 99) for _ in range(10)] for _ in range(10)]

# вивести на екран
for row in matrix:
    print(row)

# - вивести суму чисел головної діагоналі матриці
main_diagonal_sum = sum(matrix[i][i] for i in range(10))
print(f"Сума чисел головної діагоналі: {main_diagonal_sum}")

# - вивести мінімальне та максимальне значення побічної діагоналі матриці
secondary_diagonal_values = [matrix[i][9 - i] for i in range(10)]
min_secondary_diagonal = min(secondary_diagonal_values)
max_secondary_diagonal = max(secondary_diagonal_values)
print(f"Мінімальне значення побічної діагоналі: {min_secondary_diagonal}")
print(f"Максимальне значення побічної діагоналі: {max_secondary_diagonal}")

# - ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)
column_number = int(input("Введіть порядковий номер стовпця: "))
column_values = [matrix[i][column_number] for i in range(10)]
print(f"Значення з обраного стовпця: {column_values}")

# - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю (аналогічно зробити з рядком)
swap_column1 = int(input("Введіть порядковий номер першого стовпця для обміну: "))
swap_column2 = int(input("Введіть порядковий номер другого стовпця для обміну: "))

for i in range(10):
    matrix[i][swap_column1], matrix[i][swap_column2] = matrix[i][swap_column2], matrix[i][swap_column1]

# Виведення матриці після обміну
print("\nМатриця після обміну стовпців:")
for row in matrix:
    print(row)








