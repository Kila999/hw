#  Написать функцию buble_sort принимающую в качестве входящего параметра не отсортированный список
def bubble_sort(UNSORTED_LIST):
    # Алгоритм функции buble_sort должен сортировать список методом пузырьковой сортировки.
    for n in range(len(UNSORTED_LIST)-1, 0, -1):
        for i in range(n):
            if UNSORTED_LIST[i] > UNSORTED_LIST[i + 1]:
                UNSORTED_LIST[i], UNSORTED_LIST[i + 1] = UNSORTED_LIST[i + 1], UNSORTED_LIST[i]

# Написать функцию selection_sort принимающую в качестве входящего параметра не отсортированный список
def selection_sort(UNSORTED_LIST):
    # Алгоритм функции selection_sort должен сортировать список методом сортировки выбором.
    for i in range(len(UNSORTED_LIST)-1):
        min_index = i
        for j in range(i+1, len(UNSORTED_LIST)-1):
            if UNSORTED_LIST[j] < UNSORTED_LIST[min_index]:
                min_index = j
        UNSORTED_LIST[i], UNSORTED_LIST[min_index] = UNSORTED_LIST[min_index], UNSORTED_LIST[i]


UNSORTED_LIST = [21, 4, 13, 45, 32, 6, 75, 99]

# Функция buble_sort должна возвращать отсортированный список
print(f'Unsorted list is: {UNSORTED_LIST}')
bubble_sort(UNSORTED_LIST)
print(f'Sorted list by Bubble sort: {UNSORTED_LIST}')

UNSORTED_LIST = [21, 4, 13, 45, 32, 6, 75, 99]

# Функция selection_sort должна возвращать отсортированный список
print(f'Unsorted list is: {UNSORTED_LIST}')
selection_sort(UNSORTED_LIST)
print(f'Sorted by Selected sort: {UNSORTED_LIST}')