def summary():
    try:
        with open('file05.txt', 'w') as file_obj:
            line = input('Введите набор цифр через пробел \n')
            file_obj.writelines(line)
            my_number = line.split()

            print(sum(map(int, my_number)))
    except ValueError:
        print('Введите только цифры!')
summary()