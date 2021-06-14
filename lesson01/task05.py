proceeds = float(input ('Какая выручка у вашей фирмы? '))
cost = float(input ('Какая издержка у вашей фирмы? '))
profit = proceeds - cost
if profit > 0:
    print (f'Ваша фирма работает c прибылью {profit} грн.!')
    print (f'Рентабильность выручки фирмы {(profit / proceeds) * 100 :.2f} %')
    workers = int(input('Какое количество сотрудников работает в фирме? '))
    print (f'Прибыль фирмы в рассчете на одного сотрудника состовляет: {(profit / workers) :.3f} грн.')
elif profit < 0:
    print (f'Ваша фирма работает c убытоком {profit} грн.!')
else:
    print('Ноль это не минус, уже хорошо!')