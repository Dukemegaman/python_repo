playlist = list(input('Введите список '))
for i in range(len(playlist)):
    playlist[i], playlist[i + 1] = playlist[i + 1], playlist[i]
    print(f'Новый список {playlist}')