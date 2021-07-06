from abc import ABC, abstractmethod
import math

class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def raschet(self):
        pass

    def __add__(self, other):
        return self.raschet + other.raschet

class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print('Слишком маленький размер. Минимальный 40 его и считаем.')
            self.__size = 40
        elif size > 58:
            print('Слишком большой размер. Максимальный размер 58 его и считаем.')
            self.__size = 58
        else:
            self.__size = size

    @property
    def raschet(self):
        return self.__size / 6.5 + 0.5 #расход на пальто


class Jacket(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            print('Слишком маленький рост. Минимальный 150 его и считаем.')
            self.__height = 150
        elif height > 240:
            print('Слишком большой рост. Максимальный 240 его и считаем.')
            self.__height = 240
        else:
            self.__height = height

    @property
    def raschet(self):
        return (2 * self.__height + 0.3) / 100 #расход на костюм

size_v = Coat(int(input('Введите размер пальто ')))
size_h = Jacket(int(input('Введите свой рост в сантиметрах ')))
print(f'Нужно {size_v.raschet:.1f} метров ткани на пальто {size_v.size} размера')
print(f'Нужно {size_h.raschet:.1f} метров ткани на костюм для {size_h.height} см. роста')
print(f"Всего нужно  {(math.ceil(size_v + size_h))}  метров ткани")
