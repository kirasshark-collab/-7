text1 = input("Введіть текст: ")
text2 = input("Введіть другий текст: ")
norm1 = text1.lower().replace(" ", "")
norm2 = text2.lower().replace(" ", "")
if sorted(norm1) == sorted(norm2):
    print("Анаграми")
else:
    print("Не анаграми")
    