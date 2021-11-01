"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""

limit = int(input('Введите количество элементов последовательности. LIMIT = '))
summ = 0
elem = 1

def count_row_nums(row_limit, elem, summ):
   if row_limit == 0:
       return summ
   else:
       return count_row_nums(row_limit-1, -elem/2, summ+elem)

res = count_row_nums(limit, elem, summ)
print(f'Сумма элементов рядя чисел равно = {res}')
