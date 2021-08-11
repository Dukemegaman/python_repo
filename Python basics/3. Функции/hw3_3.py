def sum1(num1, num2, num3):
    sum_list = [num1, num2, num3]
    minnum = min(sum_list)
    return int(num1) + int(num2) + int(num3) - int(minnum)


print(sum1(input('Введите первое число '), input('Введите второе число '), input('Введите третье число ')))
