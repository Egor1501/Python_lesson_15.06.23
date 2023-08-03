
# Создаем словарь

key = ['Антон', 'Борис', 'Варвара', 'Игорь', 'Николай']
value = [54321, 67854, 45908, 98870, 12309]
my_dict = {}
for item in range(len(key)):
    my_dict[key[item]] = value[item]


my_dict['Борис'] =45876
my_dict['Владимир'] = 55544 #добавление абонента
print(my_dict)
