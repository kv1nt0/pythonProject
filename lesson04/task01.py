from sys import argv


def casing():
    try:
        work_h, rate, bounty = map(float, argv[1:])
        print(f'Заработная плата сотрудника -  {work_h * rate + bounty}')
    except ValueError:
        print('Введите только цифры!')


casing()
