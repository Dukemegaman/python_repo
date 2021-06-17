# Определите среднее значение всех элементов последовательности, завершающейся числом 0.
a = 0
b = 0
posled = int(input())
while posled != 0:
    a += posled
    b += 1
    posled = int(input())
print(a/b)