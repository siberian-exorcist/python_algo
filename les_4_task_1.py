"""
Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках практического задания первых трех уроков.

Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Взял последнюю задачу из 3-го урока:
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""


import timeit
import cProfile
import matplotlib.pyplot as plt
from random import randint

dots_ = []
dots_2 = []
dots_3 = []
msize = 10

def min_max_tr(n, m, start_, stop_):
    min_ = [0 * n for _ in range(m)]
    matrix_ = [[randint(start_, stop_) for _ in range(m)] for _ in range(n)]

    transpose = [[matrix_[n][m] for n in range(len(matrix_))] for m in range(len(matrix_[0]))]

    for i in range(len(transpose)):
        min_[i] = transpose[i][0]
        for j in range(len(transpose[0])):
            if transpose[i][j] <= min_[i]:
                min_[i] = transpose[i][j]

    max_ = min_[0]

    for j in range(len(min_)):
        if min_[j] >= max_:
            max_ = min_[j]


for k in range(3, msize):
    dots_.append(timeit.timeit('min_max_tr(k,k,0,100)', number=1000, globals=globals()))


plt.title("Зависимость времени выполнения алгоритма от размера матрицы.\nАлгоритм № 1")
plt.xlabel("Размер квадратной матрицы")
plt.ylabel("Времы выполнения")
plt.grid()
plt.plot(dots_)
plt.show()

cProfile.run('min_max_tr(10,10,0,10000)')

""""
cProfile.run('min_max_tr(10000,10000,0,10000)')
563846480 function calls in 188.954 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    4.727    4.727  252.990  252.990 <string>:1(<module>)
        1   18.857   18.857  248.262  248.262 les_4_task_1.py:20(min_max_tr)
        1    0.001    0.001    0.001    0.001 les_4_task_1.py:21(<listcomp>)
        1    0.034    0.034  186.403  186.403 les_4_task_1.py:22(<listcomp>)
        1    0.043    0.043   43.000   43.000 les_4_task_1.py:24(<listcomp>)
100000000   54.192    0.000   77.820    0.000 random.py:237(_randbelow_with_getrandbits)
100000000   56.644    0.000  134.464    0.000 random.py:290(randrange)
100000000   30.821    0.000  165.285    0.000 random.py:334(randint)
        1    0.000    0.000  252.990  252.990 {built-in method builtins.exec}
    20003    0.007    0.000    0.007    0.000 {built-in method builtins.len}
100000000    7.645    0.000    7.645    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
163826470   15.983    0.000   15.983    0.000 {method 'getrandbits' of '_random.Random' objects}
"""


"""
Вывод по функциии min_max_tr. Функция медленная, основное время тратится 
не генерацию матрицы и ее транспонирование
"""


def min_max(SIZE_ROW, SIZE_COL, MIN_ITEM, MAX_ITEM):
    matrix = [[randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_COL)] for _ in range(SIZE_ROW)]

    max_ = None

    for j in range(len(matrix[0])):
        min_ = matrix[0][j]

        for i in range(len(matrix)):
            if matrix[i][j] < min_:
                min_ = matrix[i][j]

        if max_ is None or max_ < min_:
            max_ = min_


for k in range(3, msize):
   dots_2.append(timeit.timeit('min_max(k,k,0,100)', number=1000, globals=globals()))

plt.title("Зависимость времени выполнения алгоритма от размера матрицы.\nАлгоритм № 2")
plt.xlabel("Размер квадратной матрицы")
plt.ylabel("Времы выполнения")
plt.grid()
plt.plot(dots_2)
plt.show()

cProfile.run('min_max(10,10,0,10000)')

"""
cProfile.run('min_max(10000,10000,0,10000)')

563837391 function calls in 197.934 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    1.393    1.393  218.619  218.619 <string>:1(<module>)
        1   34.977   34.977  217.225  217.225 les_4_task_1.py:78(min_max)
        1    0.021    0.021  182.244  182.244 les_4_task_1.py:79(<listcomp>)
100000000   52.810    0.000   75.921    0.000 random.py:237(_randbelow_with_getrandbits)
100000000   55.339    0.000  131.260    0.000 random.py:290(randrange)
100000000   30.278    0.000  161.538    0.000 random.py:334(randint)
        1    0.000    0.000  218.619  218.619 {built-in method builtins.exec}
    10001    0.004    0.000    0.004    0.000 {built-in method builtins.len}
100000000    7.525    0.000    7.525    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
163827385   15.586    0.000   15.586    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

"""
Вывод по функциии min_max. Эта функция также медленная в основном из-за времени 
на генерацию матрицы. И в целом быстрее первой реализации
"""


"""
Общий вывод
функция min_max работает быстрее, чем функция min_max_tr. 
Обе иимеют сложность алгоритма O(n * log(n)) 
"""
