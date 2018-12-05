
__author__ = 'Ковригин Сергей'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    part = len(str(number - int(number))[2:])     # дробная часть без 0,
    if int(number) == number or part <= ndigits:  # а нужно ли округлять?
        return number

    for _ in range(part - ndigits):
        it = 1 if int(str(number)[-1]) >= 5 else 0
        number = number * 10 ** part // 10 + it
        part -= 1
        number /= 10 ** (part)
    return number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    if len(str(ticket_number)) != 6 or not str(ticket_number).isdigit():
        return 'Номер должен состоять из 6 цифр'

    ticket_number = [int(i) for i in str(ticket_number)]
    if sum(ticket_number[3:]) == sum(ticket_number[:3]):
        return 'Счастливый билет'
    else:
        return 'Увы и ах...'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
