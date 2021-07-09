class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def make_order(self, rows):
        return '\n'.join(['#' * rows for _ in range(self.quantity // rows)]) + '\n' + '#' * (
                    self.quantity % rows)

    def __str__(self):
        return f'Результат операции {self.quantity}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return Cell(self.quantity - other.quantity) if (self.quantity - other.quantity) > 0 \
            else print('Вторых клеток меньше чем первых!')

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __floordiv__(self, other):
        return Cell(self.quantity // other.quantity)


c_1 = int(input('Введите количество первых клеток '))
cell_1 = Cell(c_1)
c_2 = int(input('Введите количество вторых клеток '))
cell_2 = Cell(c_2)
w = int(input('Введите количество ячеек для клеток в ряду '))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(w))
print(cell_2.make_order(w))


