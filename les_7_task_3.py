"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""

from random import uniform as rand_f

m = int(input('Введите размер m массива 2m+1. m = '))
start_ = -1000
end_ = 1000
arr_ = [round(rand_f(start_, end_), 2) for i in range(2*m+1)]
#arr_ = [1.0, 3.0, 4.0, 9.0, 5.0, 3.0, 2.0, 7.0, 2.0, 3.0, 6.0]
print(f'Исходный массив:\n {arr_}')


def mediana_1(arr):
    for i in range(len(arr)):
        cnt_less = 0
        cnt_more = 0
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] > arr[j]:
                cnt_less += 1
            elif arr[i] == arr[j]:
                cnt_less += 1
            else:
                cnt_more += 1
        if cnt_less == cnt_more:
            return arr[i]


print(f'{mediana_1(arr_)}')
