month = int(input('Введите месяц в в иле целого числа '))
list1 = ['winter', 'winter', 'spring', 'spring', 'spring',
        'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
dict2 = {1:'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring',
       6: 'summer', 7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
print(f'Месяц № {month} - {list1[month - 1]}')
print(f'{month} - {dict2[month]}')
