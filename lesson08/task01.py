class Data:
    def __init__(self, data_attribute):
        self.data_attribute = str(data_attribute)

    @classmethod
    def extract(cls, data_attribute):
        my_date = []

        for _ in data_attribute.split():
            if _ != '-': my_date.append(_)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2021:
                    return f'Всё верно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.data_attribute)}'


you_day = Data('08 - 07 - 2021')
print(you_day)
print(Data.valid(8, 7, 2021))
print(Data.valid(32, 7, 2021))
print(Data.valid(8, 13, 2021))
print(Data.valid(8, 7, 2022))
print(you_day.valid(8, 7, 2021))
print(you_day.valid(32, 7, 2021))
print(you_day.valid(8, 13, 2021))
print(you_day.valid(8, 7, 2022))
print(Data.extract('9 - 10 - 2021'))
print(you_day.extract('10 - 9 - 2021'))
