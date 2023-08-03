#Task 1
#Необходимо подготовить отчет о расходах членов семьи на новогодние праздники.
#Данные по расходам приведены в файле hw_10_test.txt в следующем формате:
#Номер в списке Фамилия и имя (или только имя) Сумма Категория товара

#Отчет должен включать следующее:
#1. Какая общая сумма расходов по каждой категории товаров?
#2. Сколько денег потратил каждый член семьи?
#3. Какое количество покупок и на какую общую сумму сделал введенный пользователем через input член семьи?

def total_expenses_by_categories(file_name: str):
    res = {}
    with open(file_name, 'r', encoding='utf-8'):
        res = file_name.split(';')
        categories = str(res[-1])
        res += categories

    return res


def total_expenses_by_users(file_name: str):
    result = {}
    with open(file_name, 'r', encoding='utf-8'):
        res = file_name.split(';')
        users = str(res[:1])
        res += users
    return result


def total_expenses_by_user_name(file_name: str):
    result = 0
    with open(file_name, 'r', encoding='utf-8'):
        res = file_name.split(';')
        users_name = str(res[:2])
        res += users_name
    return result


print(total_expenses_by_categories('hw_10_test.txt'))

print(total_expenses_by_users('hw_10_test.txt'))

print(total_expenses_by_user_name('hw_10_test.txt', input('username is ').strip()))