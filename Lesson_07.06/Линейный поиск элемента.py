#Task3
# Функция, которая выполняет линейный поиск элемента в списке целых чисел.
# Если элемент присутствует в списке, функция должна вернуть его индекс, если нет, то -1.

def find(list,e):
    if e in list:
        a = list.index(e)
    else:
        a = -1
    return a
list = [2,8,3,99,4,1]
element = 99
print(find(list,element))