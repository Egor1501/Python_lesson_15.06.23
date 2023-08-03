#Выведите на экран 10 строк с числом Pi. В первой строке должно быть 2 знака после запятой, во второй - 3 и так далее.

import math

count = 1
symbol = 2
while count <= 10:
    print("Pi = {:.{s}f}".format(math.pi, s=symbol))
    count += 1
    symbol += 1



