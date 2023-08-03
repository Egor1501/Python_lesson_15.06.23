# скрипт, который вычислит сумму всех кодов символов строки.

str = "Hello Python"
summa = 0
for letter in str:
    summa += ord(letter)
print(summa)


# 2-й вариант
x = 'Hello'
print(sum(map(ord,x)))
