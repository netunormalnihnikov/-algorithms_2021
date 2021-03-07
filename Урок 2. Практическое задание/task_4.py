"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
"""


def sum_el(n, answer=1, i=1):
    if n == 1 or n == 0:
        return print(answer)
    i /= -2
    answer = answer + i
    n -= 1
    sum_el(n, answer, i)


try:
    sum_el(int(input("Enter a natural number: ")))
except ValueError:
    print("Invalid number")
