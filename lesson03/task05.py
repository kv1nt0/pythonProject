def my_sum():
    total = 0
    exit = False
    while exit == False:
        number = input('Введите числа через пробел или Q для выхода - ').split()

        result = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                exit = True
                break
            else:
                result = result + int(number[el])
        total = total + result
        print(f'Сумма чисел {total}')
    print(f'Финальная сумма всех чисел {total}')


my_sum()
