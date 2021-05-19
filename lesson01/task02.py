numbers = int(input('Введите число которое хотите перевести в секунды, минуты и часы:'))
hours = numbers // 3600
minutes = (numbers - hours * 3600) // 60
seconds = numbers - (hours * 3600 + minutes * 60)
print(f'Время в формате чч:мм:сс {hours} : {minutes} : {seconds}')