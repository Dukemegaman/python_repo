goods = []
name_anal = []
price_anal = []
quantity_anal = []
dim_anal = []
anal = {"Название": name_anal, "Цена": price_anal, "Количество": quantity_anal, "Единицы измерения": dim_anal}
number = 0
user_answer = 'y'

while user_answer == 'y':
    name = input('Введите название товара')
    price = input('Введите цену товара')
    quantity = input('Введите количество товаров ')
    dim = input('Введите единицы измерения ')

    tovar = {'название': name, 'цена': price, 'количество': quantity, 'eд': dim}
    number += 1
    tovar_tuple = (number, tovar)

    name_anal.append(name)
    price_anal.append(price)
    quantity_anal.append(quantity)
    dim_anal.append(dim)

    goods.append(tovar_tuple)
    user_answer = input('Вы хотете продолжить ввод данных? y/n? ')
print(goods)
print(anal)




