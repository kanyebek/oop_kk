# O(1) - Константное время
# Алгоритм работает за фиксированное время, независимо от размера входных
#
# lst = [1,2,3,4,5,6,7,8,9]
# def get_element_by_index(lst, index):
#     return lst[index]
#
# print(get_element_by_index(lst, 4))
#
# # O(log n) - Логарифмическое время
# # # Часто встречается в алгоритмах использующих
# # # деление входных данных на 2, работает ток с сортированными списками
#
# def binary_search(lst, target):
#     left, right = 0, len(lst) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid+1
#         else:
#             right = mid-1
#     return -1
#
# print(binary_search(lst, 9))
#
# # O(n) - Линейное время
# # Алгоритм проходит по всем данным один раз
#
# def find_element(lst, target):
#     for i in lst:
#         if i == target:
#             return True
#     return False
#
# print(find_element(lst, 10))

lst3 = [1, 2, 51, 5, 2, 8, 7, 45]

lst3.sort()
print(lst3)


# O(n^2) - Квадратичное время
# Обычно встречаются в алгоритмах с двумя вложенными циклами

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j] + 1:#Если текущий эл-т, то меняем местамим
                lst[j], lst[j + 1] =lst[j + 1], lst[j]

bubble_sort(lst3)
print(lst3)
