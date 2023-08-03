#Task4
#  функция, которая возвращает количество слов в текстовой строке.

text = input('Введите текст строки: ')
words = text.split()
num_words = len(words)
print(num_words)


text = input('Введите текст: ')
word = text.count(" ") + 1

print(word)


def find(list,e):
    if e in list:
        a = list.index(e)
    else:
        a = -1
    return a
