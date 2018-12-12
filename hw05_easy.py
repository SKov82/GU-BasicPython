
__author__ = 'Сергей Ковригин'

import os
import shutil
import sys

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def mk_dirs(new_dir):
    if os.path.exists(new_dir):
        print(f'Невозможно создать, папка {new_dir} уже существует.')
    else:
        os.mkdir(new_dir)
        print(f'Папка {new_dir} успешно создана.')


def rm_dirs(rm_dir):
    if os.path.exists(rm_dir):
        shutil.rmtree(rm_dir)
        print(f'Папка {rm_dir} успешно удалена.')
    else:
        print(f'Невозможно удалить, папки {rm_dir} не существует.')


for i in range(1, 10):
    mk_dirs(f'dir_{i}')  # создаем 9 папок
    rm_dirs(f'dir_{i}')  # удаляем их


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def ls_dirs(key='d'):  # key='f' для вывода только файлов (реализовать)
    for i in os.listdir():
        if key == 'd':
            if os.path.isdir(i):
                print(i)
        elif key == 'a':  # key='a' для вывода всего содержимого папки
            print(i)
        else:
            print(f'{key} - неизвестный ключ.')
            break


ls_dirs()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def cp():
    file = os.path.basename((sys.argv[0]))  # имя файла, вызвавшего этот метод
    cp_path = os.path.realpath((sys.argv[0]))  # абс.путь к вызвавшему файлу
    shutil.copy(cp_path, f'Копия {file}')


# cp()
