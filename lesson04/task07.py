def factorial(number):
    fact_num = 1
    for el in range(number + 1):
        yield f'{el}! = {fact_num}'
        fact_num *= el +1

for w in factorial(int(input('Факториал числа - '))):
    print(w)