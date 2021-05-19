# Спросить у пользователя написать несколько слов через запятую
# распечатать: арбуз, пряник, солнышко
#
# 1 слово: арбуз
# 2 слово: пряник

# words = (input('Введите список слов'))
words = 'arbuz, pryanik, solnishko'
split_words = words.split(', ')
for i in range(len(split_words)):
    n = i + 1
    print(f'{n} slovo: {split_words[i]}')
print(split_words)
