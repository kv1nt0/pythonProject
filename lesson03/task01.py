def div(*args):
    try:
        arg1 = int(input('Введите первое число: '))
        arg2 = int(input('Введите второе число: '))
        w = arg1 / arg2
    except ValueError:
        return 'Value Error'
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'
    return round(w, 5)


print(f'Результат: {div()}')
