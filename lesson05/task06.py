subject = {}
with open('file06.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.replace(':', '').replace('-', '0').replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').split()
        subject[line[0]] = sum(map(int, line[1:]))
    print(f'Общее количество часов по предметам - \n{subject}')