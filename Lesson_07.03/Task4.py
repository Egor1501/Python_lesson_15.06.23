# task4
# Написать скрипт, который трехзначное целое число (вводит пользователь с клавиатуры) разделяет на отдельные цифры.
# Каждую цифру нужно вывести в отдельной строке.
# Например, если пользователь вводит число 987, скрипт должен вывести в терминал
# 9
# 8
# 7

x = int(input('number='))

print(x // 100)
print(x // 10 % 10)
print(x % 10)

x = input('number=')
print(x[0])
print(x[1])
print(x[2])
