def my_fynction(x, y):
    return 1 if y == 0 else my_fynction(x, y + 1) * 1 / x


num_1 = int(input('Введите положительное число: '))
num_2 = int(input('Введите отрицательное число: '))
print(f"Число {num_1} в степени {num_2} равняется {my_fynction(num_1, num_2)}")


def my_fynction(x, y):
    return 1 / x ** abs(y)


print(my_fynction(5, -4))
