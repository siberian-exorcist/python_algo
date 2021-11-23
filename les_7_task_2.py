"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

from random import uniform as rand_f


start_ = 0
end_ = 50
n = int(input('Введите размер массива для сортировки'))

arr_ = [round(rand_f(start_, end_), 2) for i in range(n)]  # не стал делать end_1 - 1 чтобы исключить 50.
print(f'Исходный массив:\n{arr_}\n')                       # потому что и так исключается. Проверил на n = 10000


def merge(arr_1, arr_2):
    arr_new = []
    i = 0
    j = 0
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] <= arr_2[j]:
            arr_new.append(arr_1[i])
            i += 1
        else:
            arr_new.append(arr_2[j])
            j += 1
    arr_new += arr_1[i:] + arr_2[j:]
    return arr_new


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        left = arr[:len(arr) // 2]
        right = arr[len(arr) // 2:]
    return merge(merge_sort(left), merge_sort(right))


print(f'Отсортированный по возрастанию массив:\n {merge_sort(arr_)}')
