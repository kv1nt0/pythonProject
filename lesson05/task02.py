my_mision = open('file_01.txt')
f = '"file_01.txt"' #подскажите способ вывод только имени файла в принт
line = 0
for w in my_mision:
    line += 1

    flag = 0
    word = 0
    for j in w:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0
        let = len(w)-1
    print(w, let, 'символа(ов)', 'и', word, 'слов(а)')

print(f'Всего строк(и) {line}, в файле {f}')
my_mision.close()
