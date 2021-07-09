class Storage:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, year):
        for name, equipments in self._dict.items():
            for equipment in equipments:
                if equipment.year == year:
                    equipments.remove(equipment)


class Office_Equipment:
    def __init__(self, name, make, year, ser_num):
        self.name = name
        self.make = make
        self.year = year
        self.ser_num = ser_num
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.make} {self.year} {self.ser_num}'


class Printer(Office_Equipment):
    def __init__(self, name, make, year, ser_num):
        super().__init__(name, make, year, ser_num)

    def __repr__(self):
        return f'{self.name} {self.make} {self.year} {self.ser_num}'

    def action(self):
        return 'Печатает'


class Scaner(Office_Equipment):
    def __init__(self, name, make, year, ser_num):
        super().__init__(name, make, year, ser_num)

    def action(self):
        return 'Сканирует'


class Xerox(Office_Equipment):
    def __init__(self, name, make, year, ser_num):
        super().__init__(name, make, year, ser_num)

    def action(self):
        return 'Копирует'


sklad = Storage()
scaner = Scaner('hp', '321', 2018, 'xcn9901v')
sklad.add_to(scaner)
scaner = Scaner('hp', '323', 2019, 'xcn9902v')
sklad.add_to(scaner)

printer = Printer('sony', '520', 2018, 'xcn9904v')
sklad.add_to(printer)
printer = Printer('sony', '521', 2019, 'xcn9905v')
sklad.add_to(printer)

xerox = Xerox('Epson', '721', 2019, 'xcn9907v')
sklad.add_to(xerox)
xerox = Xerox('Epson', '720', 2018, 'xcn9908v')
sklad.add_to(xerox)

print(sklad._dict)
sklad.extract(2018)
print('Произошло списание устаревших моделей.')
print(sklad._dict)
