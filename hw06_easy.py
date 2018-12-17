
__author__ = 'Сергей Ковригин'

import math


def side(P1, P2):  # длина стороны
    return math.hypot(P2[0] - P1[0], P2[1] - P1[1])


def pertr(*sides):  # периметр
    return sum(sides)


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle():
    def __init__(self, Pt):
        self.A = Pt[0]
        self.B = Pt[1]
        self.C = Pt[2]
        self.ab = side(self.A, self.B)
        self.bc = side(self.B, self.C)
        self.ca = side(self.C, self.A)
        self.P = pertr(*[self.ab, self.bc, self.ca])

    def area(self):  # площадь через формулу Герона
        p = self.P / 2
        return (p * (p - self.ab) * (p - self.bc) * (p - self.ca)) ** 0.5

    def ht(self, side):  # высота к стороне side
        return 2 * self.area() / side


# Проверки
trs = (([0, 0], [10, 10], [20, 0]),
       ([-10, -10], [0, 25], [10, -10]),
       ([0, 0], [0, 15], [20, 0]),
       ([0, 0], [-20, 15], [25, 40]))
for tr in trs:
    tr = Triangle(tr)
    print(f'A={tr.A}, B={tr.B}, C={tr.C}. ab={tr.ab}, bc={tr.bc}, ca={tr.ca}\n',
          f'S={tr.area()}, P={tr.P}, h_Abc={tr.ht(tr.bc)} h_Bca={tr.ht(tr.ca)} h_Cab={tr.ht(tr.ab)}')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapeze():
    def __init__(self, Pt):
        self.A = Pt[0]
        self.B = Pt[1]
        self.C = Pt[2]
        self.D = Pt[3]
        self.ab = side(self.A, self.B)
        self.bc = side(self.B, self.C)
        self.cd = side(self.C, self.D)
        self.da = side(self.D, self.A)
        self.P = pertr(*[self.ab, self.bc, self.cd, self.da])  # периметр

    def check(self):  # проверка равнобедренности через диагонали
        return 'Да' if side(self.A, self.C) == side(self.B, self.D) else 'Нет'

    def area(self):  # площадь: плохая формула - чувствительна к положению трапеции в пространстве (основания д.б. параллельны оси Х),
        h = (self.bc + self.da) / 2  # лучше плясать от синуса угла и половины произведения диагоналей)
        S = h * (self.ab ** 2 - (((self.da - self.bc) ** 2 + self.ab ** 2 - self.cd ** 2) / (2 * (self.bc - self.da))) ** 2) ** 0.5
        return S  # к тому же, в случае прямоугольника, выдаст ошибку деления на ноль


# Проверки
traps = (([0, 0], [10, 10], [20, 10], [30, 0]),
         ([-10, -10], [0, 25], [20, 25], [40, -10]),
         ([0, 0], [0, 15], [15, 15], [25, 0]),
         ([-15, -10], [-40, 10], [40, 10], [15, -10]))
for tr in traps:
    tr = Trapeze(tr)
    print(f'ab={tr.ab}, bc={tr.bc}, cd={tr.cd}, da={tr.da}\n',
          f'Равнобедренная трапеция? {tr.check()}, P={tr.P}, S={tr.area()}')
