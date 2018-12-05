
__author__ = 'Ковригин Сергей'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    a, b = 1, 1
    series = [0, a, b]
    for _ in range(m - 2):  # -2, т.к. первые 2 элемента 1 1
        a, b = b, a + b
        series.append(b)
    return series[n:m + 1]  # до m включительно


print(fibonacci(3, 6))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


def sort_to_max_2(lst):  # тоже самое только через for
    for n in range(1, len(lst)):
        for i in range(len(lst) - n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


lst = [2, 10, -12, 2.5, 20, -8, 4, 4, 0]
print(sort_to_max(lst))
print(sort_to_max_2(lst))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, lst):
    return [x for x in lst if func(x)]


# Проверки
a = ['data', '', ' ', 'window', 'widow', 'top', 'balcony']
print(list(filter(lambda x: len(x) > 4, a)))
print(list(my_filter(lambda x: len(x) > 4, a)))

a = [1, -4, 6, 8, -10]
def func(x):
    return 1 if x > 0 else 0

print(list(filter(func, a)))
print(list(my_filter(func, a)))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math


def side(a1, a2, a3, a4):  # стороны - Пифагорушка православный
    side1 = ((a2[0] - a1[0]) ** 2 + (a2[1] - a1[1]) ** 2) ** 0.5
    side2 = ((a3[0] - a2[0]) ** 2 + (a3[1] - a2[1]) ** 2) ** 0.5
    # side3 = ((a4[0] - a3[0]) ** 2 + (a4[1] - a3[1]) ** 2) ** 0.5
    # side4 = ((a1[0] - a4[0]) ** 2 + (a1[1] - a4[1]) ** 2) ** 0.5
    side3 = math.hypot((a4[0] - a3[0]), (a4[1] - a3[1]))
    side4 = math.hypot((a1[0] - a4[0]), (a1[1] - a4[1]))
    print('{}'.format(True if side1 == side3 and side2 == side4 else False))


def diagonal(a1, a2, a3, a4):  # диагонали - дешево и сердито
    cross1 = ((a1[0] + a3[0]) / 2, (a1[1] + a3[1]) / 2)
    cross2 = ((a2[0] + a4[0]) / 2, (a2[1] + a4[1]) / 2)
    print('{}'.format(True if cross1 == cross2 else False))


# Проверки
var = ([(0, 0), (0, 10), (10, 10), (10, 0)],  # квадрат
       [(-10, 0), (0, 15), (10, 0), (0, -15)],  # ромб
       [(0, 0), (10, 10), (30, 10), (20, 0)],  # параллелограмм
       [(-10, 0), (-5, 10), (5, 10), (10, 0)])  # трапеция
for a1, a2, a3, a4 in var:
    side(a1, a2, a3, a4)
    diagonal(a1, a2, a3, a4)
