nums = [float(input(f"Введи {i+1}-е число: ")) for i in range(3)]

choice = input("Обери опцію (max, min, avg): ")

if choice == "max":
    result = max(nums)
    print(f"Максимум: {result}")
elif choice == "min":
    result = min(nums)
    print(f"Мінімум: {result}")
elif choice == "avg":
    result = sum(nums) / len(nums)
    print(f"Середнє арифметичне: {result}")
else:
    print("Невірний вибір опції")
