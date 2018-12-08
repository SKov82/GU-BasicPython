
__author__ = 'Ковригин Сергей'

# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]

# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

print([list(i) for i in zip(*matrix)])  # Вариант 1
print([[matrix[j][i] for j in range(3)] for i in range(3)])  # Вариант 2


# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:

import random

number = [random.randint(0, 9) for _ in range(1000)]
print(''.join([str(num) for num in number]))

max_mult = 0
for i in range(996):
    mult = 1
    for num in number[i:i + 5]:
        mult *= num
    if mult > max_mult:
        max_mult = mult
        shift = i

print(f'Произведение = {max_mult}, индекс -> {shift}. Серия - {number[shift:shift + 5]}')


# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

import random


def check(var):
    x = [i[0] for i in var]
    y = [i[1] for i in var]
    c = False
    for i in range(7):
        for j in range(i + 1, 8):
            if abs(x[i] - x[j]) == abs(y[i] - y[j]) or x[i] == x[j] or y[i] == y[j]:
                c = True
    return 'YES' if c else 'NO'


# Проверки
var = [(1, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5),  # не бьют
       (7, 8), (2, 2), (8, 5), (4, 3), (5, 7), (1, 4), (6, 1), (3, 6)]  # бьют
for _ in range(16):  # еще 2 случайных набора
    var.append((random.randint(1, 8), random.randint(1, 8)))

for i in range(4):  # проверяем 4 набора из 8 пар координат
    print(var[i * 8:i * 8 + 8], check(var[i * 8:i * 8 + 8]))
