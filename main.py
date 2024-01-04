def meters_to_miles(meters):
    return meters * 0.000621371
def meters_to_inches(meters):
    return meters * 39.370078740157
def meters_to_yards(meters):
    return meters * 1.09361329834

meters = float(input("введіть метри:"))
choice = input("Обери одиниці для переведення (милі, дюйми, ярди): ")

if choice == "милі":
    result = meters_to_miles(meters)
    print(f"{meters} метрів дорівнюe {result} миль")

elif choice == "дюйми":
    result = meters_to_inches(meters)
    print(f"{meters} метрів дорівнюe {result} дюймів")

elif choice == "ярди":
    result = meters_to_yards(meters)
    print(f"{meters} метрів дорівнюe {result} ярди")

else:
    print("неірний вибір одинці")

