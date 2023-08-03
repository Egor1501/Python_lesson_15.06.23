# Дано число (четырехзначное). Проверить, является ли оно «счастливым билетом».
# Примечание: счастливым билетом называется число, в котором при четном количестве цифр сумма цифр его левой половины равна сумме цифр его правой половины.

num = input('Попытай счастье: ')
num = list(map(int,num))
if sum(num[:3]) == sum(num[3::]):
    print('Счастливый билет')
else:
    print('Обычный билет')


# 2-й вариант

num = input('Попытай счастье: ')
num = list(map(int,num))
if sum(num[:len(num)//2]) == sum(num[len(num)//2:]):
    print('Счастливый билет')
else:
    print('Обычный билет')
