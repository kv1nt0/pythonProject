class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self._income = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position


class Role(Worker):
    def full_name(self):
        return f'{self.name} {self.surname}'

    def full_income(self):
        return f'{sum(self._income.values())}'

data01 = Role('Иван', 'Петров', 'Python', 50000, 125000)
print(data01.full_name())
print(data01.position)
print(data01.full_income())