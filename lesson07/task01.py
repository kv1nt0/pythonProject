from itertools import zip_longest
import random


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*t, fillvalue=0))
                       for t in zip_longest(self.matrix, other.matrix, fillvalue=[])])


stroki = random.randint(3, 5)
stolbci = stroki
m_1 = Matrix([[r_stolb * r_strok for r_strok in range(stroki)] for r_stolb in range(stolbci)])
m_2 = Matrix([[r_stolb * r_strok for r_strok in range(stroki)] for r_stolb in range(stolbci)])

m_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_4 = Matrix([[2, 4], [5], [8, 8, 8]])

print(f'{m_1} \n')
print(m_1 + m_2)

print(f'\n{m_3}\n \n{m_4}\n')
sum_02 = m_3 + m_4
print(sum_02)