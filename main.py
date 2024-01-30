# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# result = factorial(5)
# print(result)

# def power(n, e):
#     if e == 0:
#         return 1
#     elif e > 0:
#         return n * power(n, e - 1)
#     else:
#         return 1 / (n * power(n, -e - 1))
#
# result_positiv = power(6, 2)
# result_negativ = power(6, -2)
# print(result_positiv)
# print(result_negativ)


# def stars(N):
#     if N > 0:
#         print('*', end='')
#         stars(N - 1)
#     else:
#         print()
#
# user_input = int(input("введіть  кількість потрібних зірок: "))
# stars(user_input)

# def sum_range(a, b):
#     if a > b:
#         return 0
#     else:
#         return a + sum_range(a + 1, b)
#
# a = 1
# b = 5
# print(f"сума чисел в діапазоні від {a} до {b} дорівнює {sum_range(a, b)}")

# def list:
#     if a > b:
#         return 0
#     print(list)
#     else:
#         return max

# import random
#
#
# def find_min_sequence_start(arr, start_index=0):
#
#
#     if start_index + 10 > len(arr):
#         return start_index
#
#
#     current_sequence = arr[start_index:start_index + 10]
#     current_sum = sum(current_sequence)
#
#
#     next_start_index = find_min_sequence_start(arr, start_index + 1)
#
#
#     next_sequence = arr[next_start_index:next_start_index + 10]
#     next_sum = sum(next_sequence)
#
#     return start_index if current_sum < next_sum else next_start_index
#
# random_numbers = [random.randint(1, 100) for _ in range(100)]
#
#
# start_position = find_min_sequence_start(random_numbers)
#
#
# print("Список із рандомними числами: ", random_numbers)
# print("Початкова позиція послідовності:", start_position)
# min_sequence = random_numbers[start_position:start_position + 10]
# min_sequence_sum = sum(min_sequence)
# print("Мінімальна послідовність:", min_sequence)
# print("Сума мінімальної послідовності:", min_sequence_sum)
