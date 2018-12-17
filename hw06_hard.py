
__author__ = 'Сергей Ковригин'

import os

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Worker:
    def __init__(self, name, surname, salary, position, base):
        self.name = name
        self.surname = surname
        self.salary = float(salary)  # оклад
        self.position = position  # должность
        self.base = float(base)  # норма часов
        self.hours = None  # отработано часов
        self.income = None  # заработок

    def payroll(self, hours):  # расчет з/п
        self.hours = hours
        if hours > self.base:
            self.income = self.salary * (1 + 2 * (hours / self.base - 1))
        else:
            self.income = self.salary * (hours / self.base)


def op_f(way):
    with open(os.path.join(way), 'r', encoding='UTF-8') as f:
        return f.readlines()


workers = op_f('data/workers.txt')
hours_of = op_f('data/hours_of.txt')
ws = {}  # словарь экземпляров класса Работник, ключ [Фамилия Имя]
for worker in workers[1:]:
    worker = worker.split()
    ws[f'{worker[1]} {worker[0]}'] = Worker(*worker)

for hours in hours_of[1:]:
    hours = hours.split()
    ws[f'{hours[1]} {hours[0]}'].payroll(float(hours[2]))

for worker in sorted(ws.keys()):  # Проверяем
    print(f'{ws[worker].position} {worker} с окладом {ws[worker].salary} руб. за {ws[worker].base} часов,',
          f'отработал {ws[worker].hours} часов и заработал {round(ws[worker].income, 2)} руб.')
