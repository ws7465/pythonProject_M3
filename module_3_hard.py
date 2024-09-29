#
#  Задание "Раз, два, три, четыре, пять .... Это не всё?":
#
# data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
#
#   Что должно быть подсчитано:
#
#    1.  Все числа (не важно, являются они ключами или значениям или ещё чем-то).
#    2.  Все строки (не важно, являются они ключами или значениям или ещё чем-то)
#
#
#  Для примера, указанного выше, расчёт вёлся следующим образом:
#  1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
#
#
def calculate_structure_sum(dat) :  #
    calc = 0  #
    for i in dat :  #
        if isinstance(i, int) :  #
            calc = calc + i  #
        elif isinstance(i, str) :  #
            calc = calc + len(i)  #
        elif isinstance(i, list) :  #
            calc = calc + calculate_structure_sum(i)  #
        elif isinstance(i, tuple) :  #
            i_list = list(i)  #
            calc = calc + calculate_structure_sum(i_list)  #
        elif isinstance(i, set) :  #
            i_list = list(i)  #
            calc = calc + calculate_structure_sum(i_list)  #
        elif isinstance(i, dict):  #
            i_list = [element for pair in i.items() for element in pair]  #
            calc = calc + calculate_structure_sum(i_list)  #
        else :  #
            continue  #
    return calc  #
#
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)
#
#
# Входные данные (применение функции):
# data_structure = [
# [1, 2, 3],
# {'a': 4, 'b': 5},
# (6, {'cube': 7, 'drum': 8}),
# "Hello",
# ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)
#
#
# Выходные данные (консоль):
# 99
#
# конец задания
#