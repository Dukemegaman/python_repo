def my_func(x, y):
    y = abs(y)
    i = 1
    while i < y:
        x = x * x
        i += 1
    return (1 / x)


print(my_func(input('Введите положительное число '), input('Введите целое отрицательное число ')))
