"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

Решение
n = int(input('Введите число n: '))
n2 = n + n
n3 = n + n +n
result = str(n) + str(n2) + str(n3)
print('n + nn + nnn = ', result)
