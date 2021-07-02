class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return (f'{self.name} поехала.')

    def stop(self):
        return (f'{self.name} остановилась.')

    def turn(self, direction):
        return (f'{self.name} повернула {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return (f'У {self.name} скорость движения {self.speed}.')

    def police(self):
        if self.is_police == True:
            return f'{self.name} из полицеского управления'
        else:
            return f'{self.name} не из полицеского управления'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость машины {self.name} составляет {self.speed} км/ч.')

        if self.speed > 60:
            return f'Скорость машины {self.name} больше разрешенной скорости для городских машин'
        else:
            return f'Скорость машины {self.name} разрешенная для городских машин'


class SportCar(Car):
    ''' Спортивный автомобиль '''


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость машины {self.name} составляет {self.speed} км/ч.')

        if self.speed > 40:
            return f'Скорость машины {self.name} больше разрешенной скорости для рабочих машин'
        else:
            return f'Скорость машины {self.name} разрешенная для рабочих машин'


class PoliceCar(Car):
    ''' Полицейский автомобиль '''

bmw = SportCar(180, 'Черный', 'BMW e60', True)
mazda = TownCar(70, 'Красный', 'Мазда cx-9', False)
gaz = WorkCar(40, 'Оранжевый', 'Мусоровоз ГАЗ', False)
superb = PoliceCar(110, 'Белый', 'Superb', True)
print(bmw.go())
print(bmw.turn(1))
print(bmw.show_speed())
print(f'{bmw.name} {bmw.color} цвет')
print(bmw.police())
print(bmw.stop())

print(mazda.go())
print(mazda.turn(0))
print(mazda.show_speed())
print(f'{mazda.name} {mazda.color} цвет')
print(mazda.police())
print(mazda.stop())

print(gaz.go())
print(gaz.turn(1))
print(gaz.show_speed())
print(f'{gaz.name} {gaz.color} цвет')
print(gaz.police())
print(gaz.stop())

print(superb.go())
print(superb.turn(0))
print(superb.show_speed())
print(f'{superb.name} {superb.color} цвет')
print(superb.police())
print(superb.turn(1))
print(gaz.stop())
