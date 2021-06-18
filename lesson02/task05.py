my_list = [9, 6, 5, 2, 1]
print(f'Текущий рейтинг - {my_list}')
added = int(input('Введите новое число рейтинга:'))

i = 0
for m in my_list:
    if added <= m:
        i += 1
    else:
        break
my_list.insert(i, added)
print(my_list)
