a = int(input('Введите первый результат '))
b = int(input('Введите конечноый результат '))

d = 1
nakopl_rez = a

while nakopl_rez < b:
    nakopl_rez = nakopl_rez + nakopl_rez * 0.1
    d += 1
    print(f'{d}: {nakopl_rez} km')

print(f'Потребуется {d} дней')

