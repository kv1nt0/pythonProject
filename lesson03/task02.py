def person_info(n, sn, y, c, em, p):
    return f'Имя - {n}; Фамилия - {sn}; Дата рождения - {y}; Город - {c}; Email - {em}; Телефон - {p}'


name = input('Введите Ваше имя -')
surname = input('Введите Вашу фамилию -')
year = input('Введите Ваш год рождения -')
city = input('Введите Ваш город проживания -')
email = input('Введите Вашу электронную почту -')
phone = input('Введите Ваш телефонный номер')

print(person_info(sn=surname, n=name, y=year, c=city, em=email, p=phone))
