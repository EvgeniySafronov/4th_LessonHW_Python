""" Вычислить число c заданной точностью d
Пример:

при $d = 0.001, π = 3.141 """

from math import pi
import math

f =  str(input("Введите число для примера точности числа Пи:\n"))

def get_ind(f):
    str_f = str(f)
    if '.' not in str_f:
        return 0
    return len(str_f[str_f.index('.') + 1:])


a = get_ind(f)
int(a)
print(f'Округленное число Пи: {round(pi, a)} ')