text = input("Введіть ПІБ повністю: ")
parts = text.split()
if len(parts) == 3:
    surname = parts[0].capitalize()
    first_name = parts[1][0].upper()
    patronymic_initial = parts[2][0].upper()
    print(f"{surname} {first_name}.{patronymic_initial}.")
else:
    print("Помилка")
