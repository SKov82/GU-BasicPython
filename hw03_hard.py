
__author__ = 'Ковригин Сергей'

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def fractions(frac):  # можно улучшить, но не успеваю
    frac = frac.split()
    op = '+' if frac[1] == '+' or frac[2] == '+' else '-'
    if frac[1] == op:
        if '/' in frac[0]:
            x1 = int(frac[0].split('/')[0])
            y1 = int(frac[0].split('/')[1])
        else:
            x1 = int(frac[0])
            y1 = 1

        if len(frac[2:]) == 1:
            if '/' in frac[-1]:
                x2 = int(frac[-1].split('/')[0])
                y2 = int(frac[-1].split('/')[1])
            else:
                x2 = int(frac[-1])
                y2 = 1
        else:
            n2 = int(frac[-2])
            x2 = int(frac[-1].split('/')[0])
            y2 = int(frac[-1].split('/')[1])
            x2 += n2 * y2

    else:
        n1 = int(frac[0])
        x1 = int(frac[1].split('/')[0])
        y1 = int(frac[1].split('/')[1])
        x1 += n1 * y1

        if len(frac[3:]) == 1:
            if '/' in frac[-1]:
                x2 = int(frac[-1].split('/')[0])
                y2 = int(frac[-1].split('/')[1])
            else:
                x2 = int(frac[-1])
                y2 = 1
        else:
            n2 = int(frac[-2])
            x2 = int(frac[-1].split('/')[0])
            y2 = int(frac[-1].split('/')[1])
            x2 += n2 * y2

    x1 *= y2; x2 *= y1; y1 *= y2  # общий знаменатель
    x = x1 + x2 if op == '+' else x1 - x2
    n = x // y1 if x // y1 >= 1 else ''
    if n:
        x -= n * y1
    return('{} {}/{}'.format(n, x, y1))


print(fractions('5/6 + 4/7'))
print(fractions('-2/3 - -2'))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os


def op_f(way):
    with open(os.path.join(way), 'r', encoding='UTF-8') as f:
        return f.readlines()


workers = op_f('data/workers.txt')
hours_of = op_f('data/hours_of.txt')

ws = {}
for worker in workers[1:]:
    worker = worker.split()
    ws[f'{worker[1]} {worker[0]}'] = [worker[2], worker[4]]  # Фио, з/п, нормачасов

income = {}
for hours in hours_of[1:]:
    hours = hours.split()
    worker = f'{hours[1]} {hours[0]}'  # ФИО
    base = int(ws[worker][1])          # Норма часов
    salary = int(ws[worker][0])        # З/п
    hours = int(hours[2])              # Отработано часов

    if hours > base:
        income[worker] = salary * (1 + 2 * (hours / base - 1))
    else:
        income[worker] = salary * (hours / base)

for worker, income in sorted(income.items()):
    print('{} заработал {}'.format(worker, round(income, 2)))


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os

with open(os.path.join('data/fruits.txt'), 'r', encoding='UTF-8') as f:
    fruits = f.readlines()

dct = list(map(chr, range(ord('А'), ord('Я') + 1)))  # алфавит
for char in dct:
    for fruit in fruits:
        if fruit.startswith(char):
            with open(os.path.join('data/fruits_%s.txt' % char),
                      'a', encoding='UTF-8') as f:
                f.write(fruit)
