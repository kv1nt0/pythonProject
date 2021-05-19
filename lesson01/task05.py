proceeds = float(input ('Какая выручка у вашей фирмы? '))
cost = float(input ('Какая издержка у вашей фирмы? '))
profit = proceeds - cost
if proceeds > cost:
    print (f'Ваша фирма работает в прибыль!')
if proceeds > cost:
    print (f'Рентабильность выручки фирмы {(profit / proceeds) * 100 :.2f} %')
    workers = int(input('Какое количество сотрудников работает в фирме? '))
    print (f'Прибыль фирмы в рассчете на одного сотрудника состовляет: {(profit / workers) :.2f} ')
if proceeds < cost:
    print ('Ваша фирма работает в убыток!')