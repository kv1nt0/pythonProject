number = int(input('Введите целое положительно число: '))
maxn = number % 10
while number > 0:
    number = number // 10
    if number % 10 > maxn:
        maxn = number % 10
        if number > 9:
            continue
    else:
        print('Максимальное число:', maxn)
        break
