"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

file = open('file_2.txt', 'r')
content = file.readlines()
print(f'Содержимое файла: \n{content}')
print(f'Количество строк в файле - {len(content)}')
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
file = open('file_2.txt', 'r')
content = file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
file.close()

