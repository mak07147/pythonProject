# ###################Task 14/06/2022########################
# def high_and_low(numbers):
#     list_of_numbers = numbers.split()
#     checked_numbers = []
#     while list_of_numbers:
#         current_number = list_of_numbers.pop()
#         checked_numbers.append(int(current_number))
#     return str(max(checked_numbers)) + ' ' + str(min(checked_numbers))
# print(high_and_low('1 9 3 4 -5'))
####################################################################
# def high_and_low(numbers):
#     numbers = [int(x) for x in numbers.split(" ")]
#     return str(max(numbers)) + " " + str(min(numbers))
# print(high_and_low('1 9 3 4 -5'))
###################################################################################################################

# sandwich_orders = ['safish', 'sameat', 'pastrami', 'sacheese', 'satomato', 'pastrami', 'saremba', 'pastrami']
# finished_sandwiches = []
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
#
# for sandwich in sandwich_orders:
#     finished_sandwiches.append(sandwich)
# print(finished_sandwiches)
# print("Sorry, we haven't pastrami anymore")
###############################################################
# def tower_builder(n_floors):
#     n = n_floors
#
#     if n == 1:
#         list = ['*']
#         for i in range(1, n, 2):
#             a = i * '*'
#             list.append(a.center(n))
#     elif n == 2:
#         list = []
#         for i in range(n - 1, 2 * n, 2):
#             a = i * '*'
#             list.append(a.center(2 * n - 1))
#     elif n > 2 or n % 2 != 0:
#         list = []
#         for i in range(1, 2 * n, 2):
#             a = i * '*'
#             list.append(a.center(2 * n - 1))
#     elif n > 2 or n % 2 == 0:
#         list = []
#         for i in range(1, 2 * n, 2):
#             a = i * '*'
#             list.append(a.center(2 * n - 1))
#     return list
# print(tower_builder(3))
##################################################################################
# Крутое решение к задаче выше
# def tower_builder(n):
#     return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
# print(tower_builder(5))
#######################################################################################


# Теперь все задачи решаем в этом файле

# def build_profile(first, last, **user_info):
#     """Строит словарь с информацией о пользователе."""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)
############################################################################
# Думал над простым решением очень долго!!! Не забывать расписывать на листике математику с заменой переменных.
# Очень хороший пример!!!
# Задание:
# Реализуйте функцию choice_from_range(), которая принимает строку-набор и выбирает случайный символ по индексу из ограниченного диапазона.
#
# Аргументы функции:
#
# строка-набор
# начальный индекс диапазона
# конечный индекс диапазона
# Решение:

# import random
#
# def choice_from_range(text, a, b):
#     n = b + 1
#     return random.choice(text[a:n])
# print(choice_from_range('abcdef', 3, 5))

########################################################################################
# Задача с кортежами
# def div_mod(a, b):
#     quotient = a // b
#     modulo = a % b
#     return (quotient, modulo)
#
# print(div_mod(13, 4))  # (3, 1)
############################################################################################
# Задача с кортежами
# def sort_pair(one_pair):
#     a = one_pair[0]
#     b = one_pair[1]
#     one_pair = (a, b)
#     second_pair = tuple(sorted(one_pair))
#
#     return second_pair
# print(sort_pair((5, 2)))
##############################################################################
# Задача на сигрегацию строк

# def join_numbers_from_range(a, b):
#     i = a
#     result = ''
#     while i <= b:
#         result = result + str(i)
#         i = i + 1
#     return result
# print(join_numbers_from_range(2, 10))
###################################################################################################

# Пример с заменой символа в строке

# def filter_string(text, char):
#     index = 0 # начальное значение для счетчика
#     result = '' # нулевое значение для строки
#     while index < len(text): # цикл "ОТ И ДО"
#       current_char = text[index] # переменная
#       index = index + 1 # счетчик должен увеличиваться
#       if current_char != char: # если индекс не равен заданному, тогда выполняется формула ниже: result = result + current_char
#         result = result + current_char
#     return result # в противном случае возврат пустой строки, т.е замена заданного символа на пустую строку.
# print(filter_string('If I look back I am lost', 'o'))
####################################################################################################################
# Вам будет предоставлен массив чисел. (24.06.2022)
# Вы должны отсортировать нечетные числа в порядке возрастания, оставив четные числа на их первоначальных позициях.
# Решение:
# def sort_array(some_array):
#     odd_arrs = sorted([i for i in some_array if i % 2 != 0])
#     arrs_odd = odd_arrs[::-1]
#     final_arrs = []
#     for el in some_array:
#             if el % 2 != 0:
#                 b = arrs_odd.pop()
#                 final_arrs.append(b)
#             elif el % 2 == 0:
#                 final_arrs.append(el)
#     return final_arrs
# some_array = [2, 22, 5, 1, 4, 11, 37, 0]
# print(sort_array(some_array))
# Ещё решения оптимальные к задаче выше:
# ---------------------------------------------------------
# def sort_array(arr):
#   odds = sorted((x for x in arr if x%2 != 0), reverse=True)
#   return [x if x%2==0 else odds.pop() for x in arr]
# ----------------------------------------------------------
# def sort_array(source_array):
#     odds = iter(sorted(v for v in source_array if v % 2))
#     return [next(odds) if i % 2 else i for i in source_array]
###############################################################################################################
