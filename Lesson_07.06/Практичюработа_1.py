
# User input for number of rows -> Пользовательский ввод количества строк


rows = int(input("Enter the rows:"))
# Outer loop will print number of rows -> Внешний цикл будет печатать количество строк

for i in range(0,rows+1):
# Inner loop will print number of Astrisk -> Внутренний цикл напечатает номер звездочки

    for j in range(i):
        print("*",end = '')
    print()