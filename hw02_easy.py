
__author__ = 'Ковригин Сергей Владимирович'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

lst = ["яблоко", "банан", "виноград", "киви", "крыжовник"]
tab = max(map(lambda x: len(x), lst))
for elem in lst:
    print('{}. {:>{}}'.format(lst.index(elem) + 1, elem, tab))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

l1 = [1, 'wall', 2, 'all', 'мяч', 'пять', 'опять', 1, 1, 3, 3, 'брод',
      '3', 0, '8', 2.5, 3.5, '1.0', 7.0, 11]
l2 = [3, 'football', 'ball', 1, 'бродяга', 'пять', '3', '0', 8,
      '3.5', 1.0, 2.5, 7, 11.0]

for e in l2:
    if e in l1:
        for _ in range(l1.count(e)):
            l1.remove(e)
print(l1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

l = [0, 1, 3, 5, 6, 7, 0, 9, 11, 99, 12, 85, 4, 16]
l2 = list(map(lambda x: x / 4 if x % 2 == 0 else x * 2, l))

print(l2)
