def user_data(name, surname, date, city, mail, phone):
    return name, surname, date, city, mail, phone


print(user_data(name=input('Enter your name: '), surname=input('Enter your surname: '), date=input('Enter your date: '),
                city=input('Enter your city: '), mail=input('Enter your mail: '), phone=input('Enter your phone: ')))
