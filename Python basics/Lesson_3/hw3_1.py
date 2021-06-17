def delenie(num1, num2):
    try:
        num1, num2 = int(num1), int(num2)
        delenie_num = num1 / num2
    except ValueError:
        return 'Буква писать низя, пиши число'
    except ZeroDivisionError:
        return 'На 0 делить низя'
    return delenie_num


print(delenie(input('Введите первое число '), input('Введите второе число ')))
