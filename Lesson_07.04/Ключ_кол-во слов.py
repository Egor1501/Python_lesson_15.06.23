#Task1
# программа, которая принимает строку текста и возвращает словарь, где ключами являются слова,
# а значениями - количество вхождений каждого слова в тексте.

my_text = "клара у клавы украла коралы а клава у клары украла клорнет"
my_dict = {}
for word in my_text.split(' '):
    if word in my_dict:
        my_dict[word] = my_dict[word] + 1
    else:
        my_dict[word] = 1

print(my_dict)


# 2-й вариант
my_text = input("Введите текст: ")
my_dict = {}
for word in my_text.split(' '):
    my_dict[word] = my_dict.get(word, 0) + 1
print(my_dict)


# вариант от OST Task1
text = input('text= ').lower().split()
res = {}
for item in text:
    if item not in res:
        res [item] = text.count(item)

print(res)

#Task2
vocabulary = {
    'cat' : 'кот',
    'dog': 'собака',
}

text = input('text= ').lower().split()
for item in text:
    print(vocabulary.get(item, item), end=' ')

#Task3

