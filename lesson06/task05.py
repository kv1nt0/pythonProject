class Stationary:
    def __init__(self, title='www'):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def draw(self):
        return f'Вы выбрали фирму {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def draw(self):
        return f'Вы выбрали фирму {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def draw(self):
        return f'Вы выбрали фирму {self.title}. Запуск отрисовки маркером'


stat = Stationary()
stat.draw()
pen = Pen('Lexi')
pencil = Pencil('Croco')
handle = Handle('Pilot')
print(pen.draw())
print(pencil.draw())
print(handle.draw())