translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("file04_0.txt", "w", encoding='utf-8') as new_file:
    with open("file04.txt", encoding='utf-8') as old_file:
        new_file.writelines([line.replace(line.split()[0], translate.get(line.split()[0])) for line in old_file])
