#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Сергей Ковригин'
__version__ = ' 0.1 '

import sys
from tkinter.filedialog import *
from tkinter import messagebox
from random import shuffle, sample

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""


def new_game():
    kegs = list(range(1, 91))  # набиваем 90 бочек в список
    shuffle(kegs)              # перемешиваем бочонки

    plr, p_card = get_card()   # карточка игрока
    comp, c_card = get_card()  # карточка компьютера

    var = answer('Играем в консоли - y\nИграем в gui - n\n')
    if var:
        console(kegs, plr, p_card, comp, c_card)
    else:
        gui(kegs, plr, p_card, comp, c_card)


def console(kegs, plr, p_card, comp, c_card):
    while len(plr) and len(comp):  # пока карточки игроков не опустели
        keg = kegs.pop(0)          # вырываем бочонки по очереди из перемешанного списка
        print(f'\nНовый бочонок: {keg}. (Осталось {len(kegs)})')
        print_card(p_card, '---------------Игрок---------------')
        print_card(c_card, '-------------Компьютер-------------')

        var = answer('Зачеркнуть цифру? (y/n)')  # ход игрока
        if var:
            if keg in plr:       # если номер бочонка в карточке
                plr.remove(keg)  # "зачеркиваем" это число
                p_card[p_card.index(keg)] = '--'
            else:
                game_over('Вы проиграли!')
        else:
            if keg in plr:  # если номер в карточке, но игрок его "профукал"
                game_over('Вы проиграли!')

        if keg in comp:     # ход компьютера
            comp.remove(keg)
            c_card[c_card.index(keg)] = '--'

        if len(plr) == 0 and len(comp) == 0:
            game_over('Ничья!')
        elif len(plr) == 0:
            game_over('Поздравляю, вы выиграли!')
        elif len(comp) == 0:  # Комп победил
            game_over('Вы проиграли!')


def get_card():  # наполняем карточки игроков 3 строки по 9 чисел
    lst = []     # не больше 3 чисел в каждом десятке, как в настоящем лото
    for i in range(9):
        lst += sample(range(i * 10 + 1, i * 10 + 11), 3)
    lst.sort()
    card = [[lst[i + j] for i in range(0, 27, 3)] for j in range(3)]
    for j in range(3):
        for i in sample(card[j], 4):  # удаляем по 4 числа в каждой строке
            lst.remove(i)
            card[j][card[j].index(i)] = '--'
    card = card[0] + card[1] + card[2]
    return (lst, card)


def print_card(c, pl):  # выводим карты на экран в удобочитаемом виде
    print(f'\n{pl}\n')
    s = ''
    for i in range(3):
        for j in range(9):
            s += str(c[i * 9 + j]) + '  ' if len(str(c[i * 9 + j])) == 2 else ' ' + str(c[i * 9 + j]) + '  '
        print(s)
        s = ''
    print('-----------------------------------\n')


def answer(text):  # принимает вопрос, возвращает обработанный ответ
    var = (input(text)).lower()
    if var in ('y', 'yes', 'да', 'д'):
        return True
    elif var in ('no', 'n', 'н', 'нет'):
        return False
    else:
        answer(text)


def game_over(result):
    print(result)
    var = answer('Ещё партию или на выход? (y/n)')
    new_game() if var else exit(0)


'''
GUI
'''


def gui(kegs, plr, p_card, comp, c_card):
    global root  # знаю, что моветон, но тороплюсь

    root = Tk()
    root.title('Geek Лото')
    root.resizable(0, 0)
    root.geometry('330x270' + '+' + str(round((root.winfo_screenwidth() - 330) / 2))\
                  + '+' + '150')
    root.protocol('WM_DELETE_WINDOW', lambda: root.destroy()\
                  if messagebox.askyesno('Выход?', 'Выйти из программы?') else None)

    m = Menu(root)
    root.config(menu=m)
    pt = (' Новая игра ', new_gui, ' ? ', about)
    for i in range(0, 3, 2):
        m.add_separator()
        m.add_command(label=pt[i], command=pt[i + 1])

    while len(plr) and len(comp):  # пока карточки игроков не опустели
        keg = kegs.pop(0)          # вырываем бочонки по очереди из перемешанного списка
        text = f'\nНовый бочонок: {keg}. (Осталось {len(kegs)})'
        text = make_card(text, p_card, '---------------Игрок---------------')
        text = make_card(text, c_card, '-------------Компьютер-------------')

        lab = Label(root, text=text, font='Consolas 11', fg='red')
        lab.place(x=16, y=2)

        if ask('Ваш ход', f'Новый бочонок: {keg}. (Осталось {len(kegs)})\nЗачеркнуть цифру?'):
            if keg in plr:       # если номер бочонка в карточке
                plr.remove(keg)  # "зачеркиваем" это число
                p_card[p_card.index(keg)] = '--'
            else:
                new_gui() if ask('Вы проиграли!', 'Ещё партию?') else sys.exit(0)
        else:
            if keg in plr:  # если номер в карточке, но игрок его "профукал"
                new_gui() if ask('Вы проиграли!', 'Ещё партию?') else sys.exit(0)

        if keg in comp:     # ход компьютера
            comp.remove(keg)
            c_card[c_card.index(keg)] = '--'

        if len(plr) == 0 and len(comp) == 0:
            new_gui() if ask('Ничья!', 'Ещё партию?') else sys.exit(0)
        elif len(plr) == 0:
            new_gui() if ask('Поздравляю, вы выиграли!', 'Ещё партию?') else sys.exit(0)
        elif len(comp) == 0:  # Комп победил
            new_gui() if ask('Вы проиграли!', 'Ещё партию?') else sys.exit(0)

    root.mainloop()


def about():
    messagebox.showinfo('О программе',
                        f'Игра "Geek Лото".\nВерсия  {__version__}'\
                        f'\nАвтор: {__author__}')


def ask(title, info):
    return messagebox.askyesno(title, info)


def make_card(text, c, pl):
    text += f'\n{pl}\n'
    s = ' '
    for i in range(3):
        for j in range(9):
            s += str(c[i * 9 + j]) + '  ' if len(str(c[i * 9 + j])) == 2 else ' ' + str(c[i * 9 + j]) + '  '
        text += s + '\n'
        s = ' '
    text += '-----------------------------------\n'
    return text


def new_gui():
    root.destroy()             # закрываем предыдущую партию (окно)

    kegs = list(range(1, 91))  # набиваем 90 бочек в список
    shuffle(kegs)              # перемешиваем бочонки

    plr, p_card = get_card()   # карточка игрока
    comp, c_card = get_card()  # карточка компьютера

    gui(kegs, plr, p_card, comp, c_card)


if __name__ == '__main__':
    new_game()
