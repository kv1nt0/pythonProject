def my_func(arg_1, arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_1 > arg_2 and arg_1 <= arg_3:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3


print(
    f'Сумма наибольших двух аргументов: {my_func(int(input("Введите первый аргумент: ")), int(input("Введите второй аргумент: ")), int(input("Введите третий аргумент: ")))}')
# даже не подумал про лямбду), уже на уроке увидел насколько всё проще
