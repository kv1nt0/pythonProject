from functools import reduce

my_list = [w for w in range(100, 1001, 2)]


def my_func(previous_el, el):
    return previous_el * el


print(f'Четные числа : {my_list}\nРезультат произведения всего списка {reduce(my_func, my_list)}')
