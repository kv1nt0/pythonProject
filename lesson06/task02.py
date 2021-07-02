class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation (self, mass=25, depth=5):
        return f'{self._length} длина м. * {self._width} ширина м. * {mass} кг * {depth} см = ' \
               f'{(self._length * self._width * mass * depth) / 1000} т'

road_01 = Road(100000, 40)
print(road_01.mass_calculation())