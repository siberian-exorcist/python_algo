"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint


start_ = 0
stop_ = 30

span = [randint(start_, stop_) for _ in range(start_, stop_)]
print(f'Начальный список: \n {span}\n')

max_ = [span[0], 0]
min_ = [span[0], 0]

for i in range(len(span)):
    if max_[0] < span[i]:
        max_ = [span[i], i]
    elif min_[0] > span[i]:
        min_ = [span[i], i]
    else:
        continue
print(f'\nМаксимум- {max_[0]}, индекс элемента - {max_[1]}')
print(f'\nМинимум - {min_[0]}, индекс элемента - {min_[1]}')
span[max_[1]], span[min_[1]] = span[min_[1]], span[max_[1]]
print(f'Список с перестановленными значениями минимума и максимума:\n{span}')
