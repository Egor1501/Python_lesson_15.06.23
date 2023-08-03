#скрипт, который возвращает наибольшее число из трех, введенных пользователем.

a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))

x = a
if x < b:
    x = b
if x < c:
    x = c
print(x)
