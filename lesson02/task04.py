# my_str = input('Введите строку из нескольких слов, разделенных пробелами: ')
# my_word = []
# num = 1
# for el in range(my_str.count(' ') + 1):
#    my_word = my_str.split()
#    if len(str(my_word)) <= 10:
#        print(f" {num} {my_word [el]}")
#        num += 1
#    else:
#        print(f" {num} {my_word [el] [:10]}")
#        num += 1

my_str = input('Введите строку из нескольких слов, разделенных пробелами: ').split()

for i, word in enumerate(my_str, 1):
    print(f'{i}- {word[:10]}')
