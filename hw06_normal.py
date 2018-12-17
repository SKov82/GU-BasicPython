
__author__ = 'Сергей Ковригин'

import random as rd

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


class School:
    def __init__(self, number, rooms, **classroom):  # № школы, классы, словарь классов
        self.number = number
        self.rooms = rooms
        self.classroom = classroom
        self.subject = {}  # словарь {предмет: список классов}

    def get_classroom(self, room):  # список всех учеников в классе room
        return [f'{pupils[fio].surname} {pupils[fio].name[0]}.{pupils[fio].name2[0]}.' for fio in self.classroom[room]]

    def get_subj(self, room):  # список всех предметов в классе room
        return [subj for subj in self.subject if room in self.subject[subj]]


class Person:
    def __init__(self, name, name2, surname):
        self.name = name
        self.name2 = name2
        self.surname = surname


class Pupil(Person):  # ученики
    def __init__(self, name, name2, surname, classroom, mother, father):
        Person.__init__(self, name, name2, surname)
        self.classroom = classroom
        self.mother = mother
        self.father = father

    def get_parents(self):
        return (self.mother, self.father)


class Teacher(Person):
    def __init__(self, name, name2, surname, subj):
        Person.__init__(self, name, name2, surname)
        self.subj = subj

    def get_teacher(self):
        return (f'{self.surname} {self.name} {self.name2}')


# наполняем нашу школу классами, человеками, нечеловеками
lit = ('A', 'Б', 'В')
m_names = ('Иван', 'Игорь', 'Николай', 'Александр', 'Петр', 'Максим',
           'Сергей', 'Владимир', 'Андрей', 'Евгений', 'Алексей', 'Дмитрий')
f_names = ('Татьяна', 'Ирина', 'Светлана', 'Ольга', 'Наталья', 'Мария',
           'Оксана', 'Елена', 'Анна', 'Валентина', 'Олеся', 'Надежда')
surnames = ('Иванов', 'Петров', 'Сидоров', 'Николаев', 'Путин', 'Афонин',
            'Кирюхин', 'Семенов', 'Орлов', 'Филиппов', 'Кроликов', 'Захаров')
names2 = ('Иванов', 'Игорев', 'Николаев', 'Александров', 'Петров', 'Максимов',
          'Сергеев', 'Владимиров', 'Андреев', 'Евгеньев', 'Алексеев', 'Дмитриев')
subjs = ('Математика', 'История', 'Литература', 'Физика', 'Химия',
         'География', 'Информатика', 'Физкультура', 'Биология', 'ОБЖ')

rooms = (f'{rd.randint(1, 6)}{lit[rd.randint(0, 2)]}' for _ in range(7))
rooms = sorted(list(set(rooms)))  # до 7 учебных классов от 1 до 6 (а, б или в)

classroom = {}  # словарь учеников класса Школа, ключ уч.классы
pupils = {}  # словарь экземпляров класса Ученик, ключ ФИО
for key in rooms:  # наполняем классы учениками
    pupil = []
    for _ in range(10):  # до 10 чел на класс
        if rd.randint(0, 1):
            surname = f'{surnames[rd.randint(0, 11)]}'
            name = f'{m_names[rd.randint(0, 11)]}'
            name2 = f'{names2[rd.randint(0, 11)]}ич'
            mother = f'{surname}а {f_names[rd.randint(0, 11)][0]}.{names2[rd.randint(0, 11)][0]}.'
            father = f'{surname} {name2[0]}.{names2[rd.randint(0, 11)][0]}.'
        else:
            surname = f'{surnames[rd.randint(0, 11)]}а'
            name = f'{f_names[rd.randint(0, 11)]}'
            name2 = f'{names2[rd.randint(0, 11)]}на'
            mother = f'{surname} {f_names[rd.randint(0, 11)][0]}.{names2[rd.randint(0, 11)][0]}.'
            father = f'{surname[:-1]} {name2[0]}.{names2[rd.randint(0, 11)][0]}.'
        fio = f'{surname} {name} {name2}'
        if fio not in pupil:
            pupil.append(fio)
            pupils[fio] = Pupil(name, name2, surname, key, mother, father)
    classroom[key] = sorted(pupil)
school = School(rd.randint(1, 99), rooms, **classroom)  # экземпляр класса Школа (№ школы, классы, словарь {класс: ученики})

t4r = {}  # словарь экземплярова класса Учитель, ключ предмет
subject = {}  # словарь учебных классов, ключ предмет
for subj in subjs:  # назначаем учителей на предметы
    if rd.randint(0, 1):
        surname = f'{surnames[rd.randint(0, 11)]}'
        name = f'{m_names[rd.randint(0, 11)]}'
        name2 = f'{names2[rd.randint(0, 11)]}ич'
    else:
        surname = f'{surnames[rd.randint(0, 11)]}а'
        name = f'{f_names[rd.randint(0, 11)]}'
        name2 = f'{names2[rd.randint(0, 11)]}на'
    t4r[subj] = Teacher(name, name2, surname, subj)
    lst = []
    for room in rooms:  # случайно определим список классов для предмета
        if rd.randint(0, 1):
            lst.append(room)
    school.subject[subj] = lst  # словарь {предмет: список классов}


# Проверки
# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы

print(f'В школе № {school.number} есть классы: ', school.rooms)

# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")

for room in school.rooms:  # Вариант 1 - полные ФИО
    print(f'В классе {room} учатся: ', school.classroom[room])
    print(f'{room} - {school.get_classroom(room)}')  # Вариант 2 - методом класса

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)

for i, fio in enumerate(sorted(pupils.keys()), start=1):
    room = pupils[fio].classroom
    print(f'{i}. Ученик {fio}. Класс {room}.')
    for j, subj in enumerate(school.get_subj(room), start=1):
        print(f'    {j}. Учитель {t4r[subj].get_teacher()}. Предмет - {subj}.')

# 4. Узнать ФИО родителей указанного ученика

for i, fio in enumerate(pupils.keys(), start=1):
    print(f'{i}. У ученика {fio} родители - {pupils[fio].get_parents()}.')

# 5. Получить список всех Учителей, преподающих в указанном классе

for room in school.rooms:
    print(room)
    for subj in school.get_subj(room):
        print(t4r[subj].get_teacher())
