a = int(input('Кол-во км. в первый день пробежки: '))
b = int(input('Желаемый результат в км.: '))
day = 1
result_km = a
while result_km < b:
    a = a * 0.1 + a
    day += 1
    result_km = result_km + a
print(f'Достигните цели на: {day} день')