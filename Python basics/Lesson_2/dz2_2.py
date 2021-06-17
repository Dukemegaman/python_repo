playlist = list(input('Введите список '))

list_odd = []
for i in range(len(playlist)):
    if i % 2 != 0:
        list_odd.append(i)

for i in list_odd:
    playlist[i], playlist[i - 1] = playlist[i - 1], playlist[i]
print(f'Новый список {playlist}')