#Task1
#Реализуйте функцию, принимающую два числа и строку в качестве параметров.
# Она должна вернуть конкатенацию строки с суммой чисел

def add(a, b):
    y = a + b
    return y


x, y = int(input('a= ')), int(input('b= '))
print(add(x, y))

print(add('1', '2'))

