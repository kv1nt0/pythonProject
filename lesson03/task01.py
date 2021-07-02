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

def my_func (x, y):
    try:
        w = x / y
        return w
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"
    except ValueError:
        return "Введите только цифры"
print(my_func(int(input("Введите x = ")), int(input("Введите y = "))))