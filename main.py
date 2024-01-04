print("Hello world")
print()
print('test')

# '''
# однрядковий
# багато рядковий
# коментар
# тут можно писати будьякий текст



number = int(input("Enter 3-digit number: "))

n1 = number // 100

n2 = number // 10 % 10


n2 = number % 100 // 10
n3 = number % 10

result = n1 + n2 + n3
print(f"n1: {n1} n2: {n2} n3 {n3}")
print(f"Result: {result}")

number = int(input("Enter 4-digit number: "))

n1 = number // 100

n2 = number // 10 % 10

n2 = number % 100 // 10
n3 = number % 10
n4 = number % 10

result = n1 + n2 + n3 + n4
print(f"n1: {n1} n2: {n2} n3: {n3} n:4 {n4}  ")
print(f"Result: {result}")

diagonal1 = int(input("user input diagonal1"))
diagonal2 = int(input("user input diagonal2"))

area = (diagonal1 * diagonal2) / 2

print(f"area: {area}")
