
__author__ = 'Сергей Ковригин'

import os
import sys
import shutil

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

try:
    print('sys.argv = ', sys.argv)
    print('sys.argv 0 = ', sys.argv[0])
    print('sys.argv 1 = ', sys.argv[1])
    print('sys.argv 2 = ', sys.argv[2], '\n')
except IndexError:
    print('\n')


def print_help():
    print('help - получение справки',
          'mkdir <dir_name> - создание директории',
          'ping - тестовый ключ',
          'cp <file_name> - создает копию указанного файла',
          'rm <file_name> - удаляет указанный файл',
          'cd <full_path or relative_path> - меняет текущую директорию на указанную',
          'ls - отображение полного пути текущей директории', sep='\n')


def make_dir():
    if not dir_name:
        print('Необходимо указать имя директории вторым параметром')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f'Директория {dir_name} создана')
    except FileExistsError:
        print(f'Директория {dir_name} уже существует')


def ping():
    print('pong')


def cp_file():
    if not dir_name:
        print('Необходимо указать имя файла вторым параметром')
        return
    try:
        cp_path = os.path.join(os.getcwd(), dir_name)
        shutil.copyfile(cp_path, f'Copy_{dir_name}')
        print(f'Файл {dir_name} скопирован')
    except OSError:
        print('Упс, что-то пошло не так...')


def rm_file():
    if not dir_name:
        print('Необходимо указать имя файла вторым параметром')
        return
    if input(f'Удалить {dir_name}? Да(Y)/Нет(N) ').lower() not in (('д', 'да',
                                                                    'y', 'yes')):
        return
    file_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.remove(file_path)
        print(f'Файл {dir_name} успешно удалён')
    except OSError:
        print(f'Файла {dir_name} не существует')


def ch_dir():
    if not dir_name:
        print('Необходимо указать имя директории вторым параметром')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print(f'Успешно перешли в {dir_name}')
        print(os.getcwd())
    except OSError:
        print(f'Директории {dir_name} не существует')


def ls_path():
    print(os.getcwd())


do = {
    'help': print_help,
    'mkdir': make_dir,
    'ping': ping,
    'cp': cp_file,
    'rm': rm_file,
    'cd': ch_dir,
    'ls': ls_path
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print('Задан неверный ключ')
        print('Укажите ключ help для получения справки')
else:
    print('Укажите ключ help для получения справки')
