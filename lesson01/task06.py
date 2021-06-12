while True:
    start = float(input('Кол-во км. в первый день пробежки: '))
    finish = float(input('Желаемый результат в км.: '))
    day = 1
    if start <= 0 or finish < 0:
        print('Результаты должны быть больше нуля.')
    else:
        while start < finish:
            start += start * 0.1
            day += 1
        print(f'Достигните цели на: {day} день')
        break
