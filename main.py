text = input("Введіть текст: ")
symbols = len(text)
letters = 0
digits = 0
spaces = 0
vowels = 0
for char in text:
    if char.isalpha():
        letters+=1
    if char.isdigit():
        digits+=1
    if char==" ":
        spaces+=1
    if char.lower() in "аеєиіїоуюяaeiou":
        vowels += 1
words = len(text.split())
print("Кількість символів", symbols)
print("Кількість букв:", letters)
print("Кількість цифр:", digits)
print("Кількість пробілів:", spaces)
print("Кількість голосних:", vowels)
print("Кількість слів:", words)
