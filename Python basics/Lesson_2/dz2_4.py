list1 = input('Введите строку из нескольких слов, разделённых пробелами ').split()
for i in range(len(list1)):
   print(f'{i+1} - {list1[i][:10]}')