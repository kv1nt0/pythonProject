with open('salary.txt', 'r', encoding='utf-8') as my_file: #ошибку загуглил и решли через encoding но толком понять как это устроено еще не смог
    wages = []
    low = []
    my_list = my_file.read().split('\n')
    for w in my_list:
        w = w.split()
        if int(w[1]) < 20000:
            low.append(w[0])
        wages.append(w[1])
print(f'Оклад меньше 20.000 {low}, средний оклад {sum(map(int, wages)) / len(wages)}')
