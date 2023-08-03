#скрипт, который посчитает, сколько букв "b" содержится во введенной строке текста.

text = input('Text= ')
word = text.count('о')
print(word)

#2-й вариант

count = 0
word = 'Здравствуйте! Я ваша тетя!'
for i in word:
    if i == 'а':
        count += 1

print("count 'a'= ", count)
