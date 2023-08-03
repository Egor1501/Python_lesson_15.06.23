#task5
# самое длинное слово и выведите его на экран.

str = ['ветер','разгоняет','стаи','туч']
print(max(str, key=len))

# 2-й вар.
text = input('text= ').split()
print(max(text, key=len))