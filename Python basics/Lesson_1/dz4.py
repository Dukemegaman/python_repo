a = int(input('Введите'))
b = 0
c = a

while c > 0:
    d = c % 10
    if d > b:
        b = d
    c = c // 10


print(f'Наибольшая цифра в числе {a} - {b}')