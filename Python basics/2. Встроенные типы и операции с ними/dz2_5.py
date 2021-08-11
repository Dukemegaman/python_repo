rating = [7, 5, 3, 3, 2]
user_number = int(input("Введите цифру "))
per_n = 0
for i in rating:
    if user_number <= i:
     per_n += 1
rating.insert(per_n, user_number)
print(rating)
