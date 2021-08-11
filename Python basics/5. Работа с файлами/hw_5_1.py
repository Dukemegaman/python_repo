"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

file = open('test.txt', 'w')
raw = input('Введите текст \n')
while raw:
    file.writelines(raw)
    raw = input('Введите текст \n')
    if not raw:
        break

file.close()
file = open('test.txt', 'r')
content = file.readlines()
print(content)
file.close()
