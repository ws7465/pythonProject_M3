# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
# #
# Для изменения регистра строки в Python можно использовать следующие методы:
#
#     lower() — преобразует все символы верхнего регистра в строке в их эквиваленты нижнего регистра, оставляя любые существующие символы нижнего регистра без изменений.
#
#     upper() — преобразует все строчные символы в строке в их эквиваленты в верхнем регистре, оставляя неизменными любые существующие заглавные символы.
#
#     capitalize() — делает заглавной только первую букву строки, оставляя остальные буквы строчными.
#
#
# Для изменения регистра списка в Python можно использовать следующие выражения:
#
#     Нижний регистр:
#     lowercase_list = [s.lower() for s in my_list]
#
#     Верхний регистр:
#     uppercase_list = [s.upper() for s in my_list]
#
#     Вместо `my_list` нужно подставить исходный список строк.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# print('Capybara')



# def func_with_params(a, b=2, c=None):
#     if c is None:
#         c = []
#         c.append(a)
#     print(c)
#
#
#
# func_with_params(3)
# func_with_params(4)
# func_with_params(5)
# func_with_params(6)

# Важно!
# Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных!
# В таком случае, если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же состоянии.
# def a(my_list = [])) – это приводит к ошибкам!
#
# Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)
# def append_to_list(item, list_my=None):
#   if list_my is None:
#    list_my = []
#   list_my.append(item)
# print(list_my)
#
# def args_to_list(*args):
#     args_list = list(args)
#     return args_list
#
#
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# flat_list = [element for pair in my_dict.items() for element in pair]
# print(flat_list)
#
#
# # Define a set
# my_set = {1, 2, 3, 4, 5}
# # Convert set to list
# my_list = list(my_set)
# # Print the list
# print(my_list) # Output: [1, 2, 3, 4, 5]
#
#
# a={1,3,'ty'}
# print(isinstance(a, set))
# b=[1,3,'ty']
# print(isinstance(b, list))
# c={1:'as',3:'df','ty':123}
# print(isinstance(c, dict))
# d=(1,3,'ty')
# print(isinstance(d, tuple))
#
#
# my_dict = {'a': 1, 'b': 2}
# values = list(my_dict.values())  # [1, 2]
# keys = list(my_dict.keys())      # ['a', 'b']
# pairs = list(my_dict.items())    # [('a', 1), ('b', 2)]
#
#
# # Кортежи с парами ключ-значение
# k_v_pairs = [(k, v) for k, v in my_dict.items()]
#
# # Плоский список с ключами и значениями
# flat_list = [element for pair in my_dict.items() for element in pair]
#
#