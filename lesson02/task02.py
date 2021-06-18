my_list = list(input('Введите символы без пробела - '))
print('Вы ввели: ', my_list)

swap = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1

my_list[:swap:2], my_list[1:swap:2] = my_list[1:swap:2], my_list[:swap:2]
print('Измененный список: ', my_list)
