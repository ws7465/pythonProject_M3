# Программа КАЛЬКУЛЯТОР
#
#
#
import tkinter as tk
#
window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False, False)
# button_add = tk.Button(window, text="+", width=2, height=2, command=add)
button_add = tk.Button(window, text="+", width=2, height=2 )
button_add.place(x=100, y=200)
# button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)
button_sub = tk.Button(window, text="-", width=2, height=2)
button_sub.place(x=150, y=200)
# button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)
button_mul = tk.Button(window, text="*", width=2, height=2)
button_mul.place(x=200, y=200)
# button_div = tk.Button(window, text="/", width=2, height=2, command=div)
button_div = tk.Button(window, text="/", width=2, height=2)
button_div.place(x=250, y=200)
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)
number1 = tk.Label(window, text="Введите первое число:")
number1.place(x=100, y=50)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=100, y=125)
answer = tk.Label(window, text="Ответ:")
answer.place(x=100, y=275)
window.mainloop()


#
#
# Разъяснения по программе
#
# import tkinter as tk  # импортируем встроенную графическую библиотеку
#                           под сокращенным именем tk (для простоты)
#
# window = tk.Tk()  # эта команда создаёт переменную - окно window, вызвав из
#                   библиотеки tk
#                   соответствующий объект - класс Tk() (окно будет "крутиться"
#                   отсюда и до команды  window.mainloop() - главный цикл
#                   обновления событий)
# window.title('Калькулятор')  # в переменной создадим заголовок нового окна
# window.geometry("350x350")  # определяем размер окна в пикселах
#                               (ширина и высота)
# window.resizable(False, False)  # запрет изменения размеров окна (чтобы при
#                                   изменении размера окна не сбивались элементы
#                                   созданные методом .place )
# button_add = tk.Button(window, text="+", width=2, height=2, command=add)  # создаем
#                                   переменную - кнопку "button_add" (ПРИБАВИТЬ) с
#                                   помощью метода Button библиотеки tk.
#                                   Кнопка принадлежит к окну window,
#                                   на ней надпись + , ширина 2, высота 2,
#
# button_add.place(x=100, y=200)  # размещаем кнопку по координатам 100 и 200
#                                   (кроме метода .place есть ещё два метода
#                                   размещения ВИДЖЕТОВ (кнопок, окошечек ввода и т.п.)
#                                   в библиотеке tk -это для самостоятельного изучения)
# button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)  # виджет -
#                                                                      кнопка "минус"
# button_sub.place(x=150, y=200)  #
# button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)  # виджет -
#                                                                    кнопка "умножить"
# button_mul.place(x=200, y=200)  #
# button_div = tk.Button(window, text="/", width=2, height=2, command=div) # виджет -
#                                                                   кнопка "разделить"
# button_div.place(x=250, y=200)  #
# number1_entry = tk.Entry(window, width=28)  # виджет - текстовое поле
#                                             (для ввода информации), в данном случае
#                                             для ввода первого числа.
#                                             Используем метод Entry
#                                             (однострочное текстовое поле)
#                                             библиотеки tk .
# number1_entry.place(x=100, y=75)  # размещаем первое текстовое поле
# number2_entry = tk.Entry(window, width=28)  # текстовое поле для второго числа
# number2_entry.place(x=100, y=150)  # размещаем
# answer_entry = tk.Entry(window, width=28) # текстовое поле для вывода результата
# answer_entry.place(x=100, y=300)  # размещаем
# number1 = tk.Label(window, text="Введите первое число:")  # Метка
#                                               первого текстового поля.
#                                               Используем метод Entry библиотеки tk .
# number1.place(x=100, y=50)  # размещаем метку
# number2 = tk.Label(window, text="Введите второе число:")  # Метка
#                                                        второго текстового поля.
# number2.place(x=100, y=125)  # размещаем метку
# answer = tk.Label(window, text="Ответ:")  # Метка текстового поля результата
# answer.place(x=100, y=275)  # размещаем метку
# window.mainloop()  # конец главного цикла обновления событий в окне
##
