"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать
ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

n = 5
m = 4
summ_ = 0

matrix_ = [[0] * m for i in range(n)]
print(matrix_)
for i in range(n):
    for j in range(m-1):
       matrix_[i][j] = (int(input(f'Введите символы {i+1} строки: ')))
print(f'Начальная матрица {n}x{m}:\n{matrix_}\n')

for i in range(n):
    for j in range(m-1):
        summ_ += matrix_[i][j]
    matrix_[i][m-1] = summ_
    summ_ = 0

print(f'Результирующая матрица:\n {matrix_}')