# Cкрипт, который спрашивает у пользователя его возраст и проверяет, соответствуют ли его данные критериям
# для получения водительского удостоверения.
# Критерии: пользователь должен быть старше 18 лет и иметь водительское удостоверение.
# Если пользователь удовлетворяет критериям, вывести сообщение "Вы можете получить водительское удостоверение".
# Если пользователь не удовлетворяет критериям, вывести сообщение "Вы не соответствуете критериям для получения
# водительского удостоверения".

x = int(input('Введи, сколько Вам лет: '))
if x >= 18:
    print('Вы можете получить водительское удостоверение')
elif x <= 18:
    print('Вы не соответствуете критериям для получения водительского удостоверения')

# 2-й вариант
age = input('Сколько Вам лет: ')
driver = input('Есть ли стаж вождения, "Да" или "Нет" : ')
if age >= '18' and driver == 'да':
    result = 'Вы можете получить водительское удостоверение'
else:
    result = 'Вы не соответствуете критериям для получения водительского удостоверения'
print(result)
