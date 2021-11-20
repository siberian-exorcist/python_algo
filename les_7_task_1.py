"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными
числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""


from random import randint

start_ = -100
end_ = 100
n = int(input('Введите размер массива для сортировки'))

arr_ = [randint(start_, end_-1) for i in range(n)]
print(f'Исходный массив:\n{arr_}\n')

def buble_sort(arr):
    """
    >>> buble_sort([94, 55, 42, -50])
    [94, 55, 42, -50]
    """
    j = len(arr)-1
    while j > 0:
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        j -= 1
    return arr

print(f'Отсортированный по убыванию массив:\n {buble_sort(arr_)}\n')

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)