# seasons_list = ['Winter', 'Spring', 'Summer', 'Autumn']
# seasons_dict = {'1': "Winter", '2': "Spring", '3': "Summer", '4': "Autumn"}
# month = int(input('Введите месяц по номеру '))

# if month == 12 or month == 1 or month == 2:
#    print(seasons_list[0])
#    print(seasons_dict.get('1'))
# elif month == 3 or month == 4 or month == 5:
#    print(seasons_list[2])
#    print(seasons_dict.get('2'))
# elif month == 6 or month == 7 or month == 8:
#    print(seasons_list[2])
#    print(seasons_dict.get('3'))
# elif month == 9 or month == 10 or month == 11:
#    print(seasons_list[3])
#    print(seasons_dict.get('4'))
# else:
#    print('В году 12 месяцев!')

seasons_dict = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}

month_num = int(input('Введи номер месяца: '))

if month_num = in sum(seasons_dict.values(), []):
    for i in seasons_dict.items():
        if month_num in i[1]:
            print(i[0])
