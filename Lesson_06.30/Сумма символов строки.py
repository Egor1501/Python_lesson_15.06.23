# Task3
# скрипт, который вычислит сумму всех кодов символов строки.

str = "Hello Python"
summa = 0
for letter in str:
    summa += ord(letter)
print(summa)

# 2-й вариант
text = input('text=')
print(sum(map(ord, text)))