#Есть девятиэтажный дом, в котором 4 подъезда. Номер подъезда начинается с единицы. На одном этаже – 4 квартиры.
# Напишите программу, которая от пользователя получает номер квартиры и выводит для заданной квартиры номер подъезда, этаж и номер на этаже.
# Если таковой квартиры нет в этом доме, то нужно вывести соответствующее сообщение

fl_num = int(input("Enter the flat number: "))

st = 0

if 1 <= fl_num <= 36:
    ent = 1
    st = (fl_num -1)//4 + 1
    print("Flat is locaterd on store",st,", entrance",ent)
elif 37 <= fl_num <= 72:
    ent = 2
    st = (fl_num - 37)//4 + 1
    print("Flat is locaterd on store",st,", entrance",ent)
elif 73 <= fl_num <= 108:
    ent = 3
    st = (fl_num - 73)//4 + 1
    print("Flat is locaterd on store",st,", entrance",ent)
elif 109 <= fl_num <= 144:
    ent = 4
    st = (fl_num - 109)//4 + 1
    print("Flat is locaterd on store",st,", entrance",ent)
else:
    print("There is no flat with number you've entered")
