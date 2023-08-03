# Задача. Посчитать сумму затрат

expenses = ['1 Bob Simson 19.58$ decoration',
            '2 Mary 66.7$ food',
            '3 Gary 98.91$ toys',
            '4 Alexa 72.29$ drinks',
            '5 Maria Simson 84.48$ food']

summa = 0

for line in expenses:
    res = line.split()
    money = float(res[-2].rstrip('$'))
    summa += money

print(f'Total:{summa:.2f}$')
