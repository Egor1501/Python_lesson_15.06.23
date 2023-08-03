# Создаем словарь

x = {1: 'пн', 2: 'вт',3: 'ср'}
day = int(input('day: '))
if day in x:
    print(x[day])
else:
    print(None)


