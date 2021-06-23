"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def summury():
    try:
        with open('file_5.txt', 'w+') as file:
            line = input('Введите цифры через пробел \n')
            file.writelines(line)
            my_numb = line.split()

            print('Сумма чисел равно', sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


summury()
