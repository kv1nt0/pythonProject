class MyComplex:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        other = other.__complex

        complex_ = self.__complex + other
        return MyComplex(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        other = other.__complex

        complex_ = self.__complex * other
        return MyComplex(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.__complex.__str__()


print(complex(6, -4) + complex(6, -5))
print(complex(5, -1) * complex(5, 6))
