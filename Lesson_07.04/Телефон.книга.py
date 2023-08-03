# Task 3
# Реализуйте простую программу для сохранения контактов.
# Каждый контакт может иметь имя в качестве ключа и номер телефонав качестве значения.
# Позвольте пользователю добавлять новые контакты, удалять существующие и получать номер телефона по имени.

# вариант кортеж

key = ['Антон', 'Борис', 'Варвара', 'Игорь', 'Николай']
value = [54321, 67854, 45908, 98870, 12309]
my_dict = {}
for item in range(len(key)):
    my_dict[key[item]] = value[item]

print(my_dict)
my_dict['Борис'] = 45876 # изминение данных
my_dict['Владимир'] = 55544 #добавление абонента
print(my_dict['Антон']) # вызов по ключу
print(my_dict)


# 2-й вариант ключ: значение

k = ['kiev', 'odessa', 'vodafon','kievstar', 'lycamobile', 'lifecell']
#'kiev' - 044
#'odessa'- 048
#'vodafon' - 050
#'kievstar' - 067
#'lycamobile' - 091
#'lifecell' - 068

d = {
    # key; value
    'kiev': 8044,
    'odessa': 8048,
    'vodafon': 8050,
    'kievstar': 8067,
    'lycamobile': 8091,
    'lifecell': - 8068,
}
print(d)
print(d['lycamobile'])



