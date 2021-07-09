class Number:
    def __init__(self, divider, dividend):
        self.divider = divider
        self.dividend = dividend

    @staticmethod
    def divide_by_null(divider, dividend):
        try:
            return(divider / dividend)
        except:
            return (f"Деление на ноль недопустимо!")


divider_01 = int(input("Введите делимое: "))
dividend_01 = int(input("Введите делитель: "))

print(Number.divide_by_null(divider_01, dividend_01))
