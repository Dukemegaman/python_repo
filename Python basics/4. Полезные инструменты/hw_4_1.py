"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, productivity, rate, bounty = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", productivity)
print("Ставка в час: ", rate)
print("Премия: ", bounty)
print("Зарплата сотрудника: ", (int(productivity) * int(rate)) + int(bounty))
