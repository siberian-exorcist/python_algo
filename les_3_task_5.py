"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint


n = 4
m = 4
start_ = 0
stop_ = 100
min_ = [0 * n for i in range(m)]
matrix_ = [[randint(start_, stop_) for _ in range(m)] for _ in range(n)]
print(f'Начальная матрица {n}x{m}:\n{matrix_}\n')

transpose = [[matrix_[n][m] for n in range(len(matrix_))] for m in range(len(matrix_[0]))]
# print(transpose)
for i in range(len(transpose)):
    min_[i] = transpose[i][0]
    for j in range(len(transpose[0])):
        if transpose[i][j] <= min_[i]:
            min_[i] = transpose[i][j]
# print(min_)
max = min_[0]
for i in range(len(min_)):
    if min_[i] >= max:
        max = min_[i]
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы равен - {max} ')
