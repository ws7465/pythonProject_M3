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



def func_with_params(a, b=2, c=None):
    if c is None:
        c = []
        c.append(a)
    print(c)



func_with_params(3)
func_with_params(4)
func_with_params(5)
func_with_params(6)

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

