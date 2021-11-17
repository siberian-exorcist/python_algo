"""
2). Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать
соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:

"""


import timeit
import cProfile
import matplotlib.pyplot as plt


dots_ = []
dots_2 = []
serial_number = int(input("Введите порядковый номер просто числла, которое хотите найти"))


def eratosthenes(n):
    sieve = list(range(n*100))
    res = []
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    for j in range(len(sieve)):
        if sieve[j] != 0:
            res.append(sieve[j])
    return res[n-1]


print(f'Метод Эратосфена.\nПростое число с порядковым номером {serial_number} равно {eratosthenes(serial_number)}\n')

"""
print(timeit.timeit('eratosthenes(100)', number=1000, globals=globals()))  # 2.5599117920000003
print(timeit.timeit('eratosthenes(500)', number=1000, globals=globals()))  # 14.840508593
print(timeit.timeit('eratosthenes(1000)', number=1000, globals=globals()))  # 27.709525015
print(timeit.timeit('eratosthenes(2000)', number=1000, globals=globals()))  # 68.027514008
print(timeit.timeit('eratosthenes(10000)', number=1000, globals=globals()))  # 411.38561679300005
"""

# cProfile.run('eratosthenes(2332493)')
"""
       25622483 function calls in 126.048 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    2.460    2.460  126.048  126.048 <string>:1(<module>)
        1  121.655  121.655  123.588  123.588 les_4_task_2.py:23(eratosthenes)
        1    0.000    0.000  126.048  126.048 {built-in method builtins.exec}
 12811240    0.996    0.000    0.996    0.000 {built-in method builtins.len}
 12811239    0.937    0.000    0.937    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

# Каких либо особенностей при профилирование не отметил для себя

"""
for k in range(3, 100000, 10000):
    dots_.append(timeit.timeit('eratosthenes(k)', number=1, globals=globals()))


plt.title("Зависимость времени выполнения алгоритма от порядкового номера простого числа.\nАлгоритм Эратосфена")
plt.xlabel("Порядковый номер простого числа x 10000")
plt.ylabel("Времы выполнения")
plt.grid()
plt.plot(dots_)
plt.show()
"""

# Сложность алгоритма характерируется, скорее всего, близкой к линейной зависимостью


def isprime(n):
    if n % 2 == 0:
        return 0
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def num_prime(n):
    cnt_ = 0
    for i in range(n * 100):
        if cnt_ == n:
            return i-1
        if isprime(i):
            cnt_ += 1


print(f'Альтернативный метод нахождения i-го простого числа.\n '
      f'Простое число с порядковым номером {serial_number} равно {num_prime(serial_number)}')
""""
print(timeit.timeit('num_prime(100)', number=1000, globals=globals()))  # 0.20050290700000017
print(timeit.timeit('num_prime(500)', number=1000, globals=globals()))  # 2.0356326780000003
print(timeit.timeit('num_prime(1000)', number=1000, globals=globals()))  # 5.377370672
print(timeit.timeit('num_prime(2000)', number=1000, globals=globals()))  # 15.300611409999998
print(timeit.timeit('num_prime(10000)', number=1000, globals=globals()))  # 175.488960022
"""

# cProfile.run('num_prime(2332493)')
"""
 38234478 function calls in 727.881 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  727.881  727.881 <string>:1(<module>)
 38234474  719.910    0.000  719.910    0.000 les_4_task_2.py:86(isprime)
        1    7.971    7.971  727.881  727.881 les_4_task_2.py:95(num_prime)
        1    0.000    0.000  727.881  727.881 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

# функция определения простого числа isprime работает быстро))

"""
for k in range(3, 100000, 10000):
    dots_2.append(timeit.timeit('num_prime(k)', number=1, globals=globals()))


plt.title("Зависимость времени выполнения алгоритма от порядкового номера простого числа.\nАльтернативный алгоритм")
plt.xlabel("Порядковый номер простого числа  x 10000")
plt.ylabel("Времы выполнения")
plt.grid()
plt.plot(dots_2)
plt.show()
"""

# Сложность алгоритма характерируется, скорее всего, n*log(n)

# Общий вывод: альтернативный алгоритм работает в разы быстрее на малых значениям тестовых данных,
# но с увеличение номера простого числа время выполнения начинает относительно быстрее расти.
# Предполагаю, что на больших номерах простых чисел алгоритм Эратосфена покажет лучший результат.
# На номере 2332493 алгорит Эратосфена отработал приблизительно в 5 раз быстрее.
