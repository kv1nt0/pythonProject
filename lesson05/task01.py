my_mision = open('file_01.txt', 'w')
while True:
    add_str = input('Введите данные - ')
    if add_str == '':
        break
    my_mision.write(add_str+'\n')
my_mision.close()
