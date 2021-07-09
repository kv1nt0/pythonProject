from random import randint
random_list = [randint(-20, 20) for el in range(10)] # понравился random), не нужно самому писать...
unique_list = [w for w in random_list if random_list.count(w) == 1]
print(f'То что было сгенерировано {random_list}')
print(f'Уникальные числа {unique_list}')
