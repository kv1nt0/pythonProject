from itertools import count, cycle

my_range = count(4)
for w in range(6):
    print('Целые числа, начиная с 4 = {}'.format(next(my_range)))
my_range = count(2)
my_value = cycle('abcdef')
for s in range(8):
    print('Повтор элементов списка  = {},{}'.format(next(my_range), next(my_value)))
