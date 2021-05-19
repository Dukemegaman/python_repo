# На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список,
# в котором содержатся только те числа, которые больше 5 по модулю.

num_list = [1, -4, 7, 3, -7]
num2_list = []
for num in num_list:
    if abs(num) > 5:
        num2_list.append(num)
print(num2_list)