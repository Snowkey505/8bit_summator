# Автор программы: Сойников Павел, ИУ7-24Б
# Назначение программы: данная программа имитирует работу восьмиразрядного сумматора для целых чисел
# с графическим интерфейсом (Tkinter). На экран выводятся все промежуточные результаты работы сумматора, позволяющие
# увидеть, как был получен ответ (или увидеть в каком месте произошла ошибка и невозможность получения этого ответа).
# Реализован ввод с помощью как физической, так и экранной клавиатуры с проверкой данных непосредственно при вводе.
# Так как сумматор восьмиразрядный, то максимальное допустимое число при вводе = 127, минимальное = -127.
# Выражение 20+ приравнивается к 20 + 0, 20- = 20 - 0.


import tkinter as tk
import re
from math_functions import bin_to_dec, dec_to_bin, bonus_code, bin_sum, summator


# Функция сумматора или удаления значений (в зависимости от флага)
def result_answer(action):
    error_input_window = False
    solution = tk.Frame(window, width=370, height=520, bg="#111")  # Фрагмент решения
    error_input = False  # Плохие данные (пустой ввод или одно число без знака + или - с краю
    # (данный ввод можно интерпретировать как 0 + 5 или 2 - 0 )

    text = field.get()
    text_copy = text.replace("-", "+")

    if text_copy.count("+") == 0 or text_copy.count("+") == 1 and len(text) == 1:
        action = "destroy"
        if len(text) != 0:
            error_input = True
        a = b = 0

    if action == "create":  # Получение числел a и b из ввода

        neg_a = neg_b = False
        a = b = 0

        if text_copy.count("+") == 1 and text_copy[0] == "+":
            if text[0] == "+":
                b = int(text.strip("+"))
            else:
                b = - int(text.strip("-"))

        else:
            i = 0
            if text != "" and text[0] == "-":
                neg_a = True
                i = 1
            elif text != "" and text[0] == "+":
                i = 1
            while i < len(text) and text[i].isdigit():
                a = a*10 + int(text[i])
                i += 1
            if text != "" and text[i] == "-":
                neg_b = True
            i += 1
            while i < len(text):
                b = b*10 + int(text[i])
                i += 1
            if neg_a:
                a *= -1
            if neg_b:
                b *= -1
            # print(a, b)

    solution.place(x=480, y=15)

    if action == "create":  # Сумматор (запись значений в переменные для дальнейшего вывода на экран)

        # Десятичные коды
        a_bin = dec_to_bin(a)
        b_bin = dec_to_bin(b)

        # Доп коды
        a_b = bonus_code(a_bin)
        b_b = bonus_code(b_bin)

        # Сумма доп кодов
        summ = bin_sum(a_b, b_b)

        # Доп код от суммы
        res_bin = bonus_code(summ)

        # В десятичную
        res = bin_to_dec(res_bin)

        # Создание виджетов с данными
        window.geometry('950x710')
        lbl_sol = tk.Label(solution, text="Ход решения", font=("Arial", 20), bg="#000", fg="white", width=22)
        bonus_codes = tk.Label(solution, text="Дополнительные коды:", font=("Arial", 15), bg="#111", fg="white", width=22)
        bonus_summ_lbl = tk.Label(solution, text="Дополнительный код:", font=("Arial", 15), bg="#111", fg="white", width=22)
        sum_text_lbl = tk.Label(solution, text="Сумма:", font=("Arial", 15), bg="#111", fg="white", width=22)

        a_ = tk.Label(solution, text=f"{a}", font=("Arial", 40), bg="#001", fg="white", width=4, relief="ridge")
        b_ = tk.Label(solution, text=f"{b}", font=("Arial", 40), bg="#001", fg="white", width=4, relief="ridge")

        a_bin_lbl = tk.Label(solution, text=a_bin, font=("Arial", 40), bg="#001", fg="white", width=8, relief="ridge")
        b_bin_lbl = tk.Label(solution, text=b_bin, font=("Arial", 40), bg="#001", fg="white", width=8, relief="ridge")

        a_bonus = tk.Label(solution, text=a_b, font=("Arial", 35), bg="#001", fg="white", width=15, relief="ridge")
        b_bonus = tk.Label(solution, text=b_b, font=("Arial", 35), bg="#001", fg="white", width=15, relief="ridge")

        summ_lbl = tk.Label(solution, text=summ, font=("Arial", 35), bg="#001", fg="white", width=15, relief="ridge")

        # b_summ = bonus_code_check_only_bin(summ)

        summ_bonus = tk.Label(solution, text=res_bin, font=("Arial", 35), bg="#001", fg="white", width=15,
                              relief="ridge")

        answer_lbl = tk.Label(window, text="Ответ:", font=("Arial", 40), bg="#111", fg="white", width=11, relief="ridge")
        result = tk.Label(window, width=13, bg="#FFF", fg="#001", font=("Arial", 40), borderwidth=2, justify="center",
                          relief="ridge")

        result["text"] = res

        # Переполнение
        if res == '-':
            result["text"] = "-Переполнение-"
            overflow = tk.Toplevel()
            overflow.title("Переполнение")
            overflow.geometry('400x150')
            overflow.configure(bg="#111")
            overflow_txt = tk.Label(overflow, text="Ошибка! Программа не может\n"
                                                 "найти значение выражение так\n"
                                                 "как происходит переполнение\n"
                                                 "(ответ > 127 или < -127)!\n"
                                                 "Введите другое выражение!", font=("Arial", 15), bg="#111", fg="red")
            overflow_txt.pack(anchor="center", pady=10)
            overflow.grab_set()
            overflow.protocol("WM_DELETE_WINDOW", lambda: on_closing(overflow))

    else:

        # Удаление текста в полях
        lbl_sol = tk.Label(solution, text="", font=("Arial", 20), bg="#111", fg="white", width=22)
        bonus_codes = tk.Label(solution, text="", font=("Arial", 15), bg="#111", fg="white",
                               width=22)
        bonus_summ_lbl = tk.Label(solution, text="", font=("Arial", 15), bg="#111", fg="white",
                                  width=22)
        sum_text_lbl = tk.Label(solution, text="", font=("Arial", 15), bg="#111", fg="white", width=22)

        a_ = tk.Label(solution, text=f"", font=("Arial", 40), bg="#111", fg="white", width=4)
        b_ = tk.Label(solution, text=f"", font=("Arial", 40), bg="#111", fg="white", width=4)

        a_bin_lbl = tk.Label(solution, text="", font=("Arial", 40), bg="#111", fg="white", width=8)
        b_bin_lbl = tk.Label(solution, text="", font=("Arial", 40), bg="#111", fg="white", width=8)

        a_bonus = tk.Label(solution, text="", font=("Arial", 35), bg="#111", fg="white", width=15)
        b_bonus = tk.Label(solution, text="", font=("Arial", 35), bg="#111", fg="white", width=15)

        summ_lbl = tk.Label(solution, text="", font=("Arial", 35), bg="#111", fg="white", width=15)

        summ_bonus = tk.Label(solution, text="", font=("Arial", 35), bg="#111", fg="white", width=15)

        answer_lbl = tk.Label(window, text="", font=("Arial", 40), bg="#111", fg="white", width=11)
        result = tk.Label(window, text="", width=13, bg="#111", fg="#111", font=("Arial", 40), borderwidth=2,
                          justify="center")

        # Плохой ввод
        if error_input:
            error = tk.Toplevel()
            error.title("Неверный ввод")
            error.geometry('400x100')
            error.configure(bg="#111")

            err_txt = tk.Label(error, text="Ошибка! Не удалось вычислить\n"
                                           "выражение из-за некорректного\n"
                                           "ввода! Попробуйте заново", font=("Arial", 15),
                               bg="#111", fg="red")
            err_txt.pack(anchor="center", pady=10)

            error.grab_set()
            error.protocol("WM_DELETE_WINDOW", lambda: on_closing(error))

    # Размещение окон вывода
    lbl_sol.grid(row=0, column=0, columnspan=2, pady=5)

    a_.grid(row=1, column=0, pady=3)
    a_bin_lbl.grid(row=1, column=1, pady=3)

    b_.grid(row=2, column=0, pady=2)
    b_bin_lbl.grid(row=2, column=1, pady=2)

    bonus_codes.grid(row=3, column=0, columnspan=2, pady=2)

    a_bonus.grid(row=4, column=0, columnspan=2, pady=2)
    b_bonus.grid(row=5, column=0, columnspan=2, pady=2)

    sum_text_lbl.grid(row=6, column=0, columnspan=2, pady=2)
    summ_lbl.grid(row=7, column=0, columnspan=2, pady=2)

    bonus_summ_lbl.grid(row=8, column=0, columnspan=2, pady=2)
    summ_bonus.grid(row=9, column=0, columnspan=2, pady=2)

    answer_lbl.place(x=70, y=620)
    result.place(x=480, y=620)


# Ввод через ENTER
def enter_input(event):
    result_answer("create")


# Очистка вывода
def clear_output():
    result_answer("destroy")


# Очистка полей ввода и вывода
def clear_all():
    button_click("C")  # Очистка ввода
    result_answer("destroy")  # Очистка вывода


# Освобождает взаимодействие с главным экраном во время закрытия верхнего
def on_closing(root):
    root.grab_release()
    root.destroy()


# Функция создания окна с информацией о программе и об авторе
def information():
    info_window = tk.Toplevel(window)
    info_window.title("О программе")
    info_window.geometry('650x320')
    info_window.resizable(False, False)
    info_window.configure(bg="#111")

    info_window.grab_set()
    info_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(info_window))

    inf_txt = tk.Label(info_window, text="Данная программа имитирует работу восьмиразрядного сумматора\n"
                                         "для целых чисел с графическим интерфейсом (Tkinter). На экран\n"
                                         "выводятся все промежуточные результаты работы сумматора,\n"
                                         "позволяющие увидеть, как был получен ответ (или увидеть в каком\n"
                                         "месте произошла ошибка и невозможность получения этого ответа).\n"
                                         "Реализован ввод с помощью как физической, так и экранной\n"
                                         "клавиатуры с проверкой данных непосредственно при вводе.\n"
                                         "Реализовано меню с основными функциями (результат, очистка, инфо).\n"
                                         "Так как сумматор восьмиразрядный, то максимальное допустимое\n"
                                         "число при вводе = 127, минимальное = -127.\n"
                                         "Выражение 20+ приравнивается к 20 + 0, 20- = 20 - 0. При вводе\n"
                                         "одного числа без знаков (20) и запуске программа выдаёт ошибку.\n"
                                         "Автор программы: Сойников Павел, ИУ7-24Б",
                       font=("Arial", 14), width=70, background="#111", foreground="white")
    inf_txt.pack(anchor="center", pady=10)


# Проверка на валидность ввода
def is_valid(text):
    if len(text) == 0:
        return True
    if text in ["-", "+"]:
        return True
    text = text.replace("-", "+")
    # print(text)
    if text.count("+") > 2:
        return False
    if text.count("+") > 1 and text[0] != "+":
        return False
    if "++" in text:
        return False
    numbers_list = text.strip("+").split("+")
    # print(numbers_list)
    for it in range(len(numbers_list)):
        try:
            elem = int(numbers_list[it])
            if elem == 0 and len(numbers_list[it]) > 1:
                return False
        except ValueError:
            return False
        if len(numbers_list[it]) == 0:
            return False
        if elem > 127:  # Слишком большое число для восьмиразрядного сумматора (1 разряд - знаковый)
            return False
    return True


# Действие при нажатии кнопки клавиатуры (кроме C all, c out, i)
def button_click(i):
    if i == "<":
        field.delete(len(field.get())-1)  # Стереть последний символ
    elif i == "C":
        field.delete(0, len(field.get()))  # Стереть поле ввода
    elif i == "=":
        try:
            result_answer("create")  # Получение ответа
        except IndexError:
            print("______")
    else:
        field.insert(tk.END, i)  # Добавление символа в ввод


# Создание окна и его виджетов
window = tk.Tk()
window.title("Восьмиразрядный сумматор")
window.geometry('500x700')
window.resizable(False, False)
window.iconphoto(False, tk.PhotoImage(file='icon_02.png'))
lbl = tk.Label(window, text="Введите выражение вида [+-] A [+-] B,\n где 0 <= A < 128 и 0 <= B < 128, целые:",
               font=("Arial", 15), background="#111", foreground="white", justify="center") # Приглашение к вводу

mainmenu = tk.Menu(window)  # Создание меню
window.config(menu=mainmenu, bg="#111")


# Виджеты меню
mainmenu.add_command(label="Вычислить", background="black", command=lambda x="=": button_click(x))
clear_menu = tk.Menu(mainmenu, tearoff=0)  # Очистка
mainmenu.add_cascade(label="Очистить", menu=clear_menu)
clear_menu.add_command(label="Поле ввода", command=lambda x="C": button_click(x))
clear_menu.add_command(label="Поле вывода", command=clear_output)
clear_menu.add_command(label="Всё", command=clear_all)
mainmenu.add_command(label="О программе", background="black", command=information)

# Проверка ввода
check = window.register(is_valid)

# Поле ввода с проверкой
field = tk.Entry(window, validate="key", validatecommand=(check, "%P"), width=11,  bg="#000", fg="white", font=("Arial", 40),
                 borderwidth=2, relief="ridge", justify="center", selectbackground="#334", selectforeground="#999")

# Фрагмент окна для клавиатуры
keyboard = tk.Frame(window, width=350, height=400, bg="#000", borderwidth=2, relief="ridge")

# Размещение на окне
lbl.pack(anchor="nw", pady=20, padx=65)
field.pack(anchor="nw", padx=80)
keyboard.pack(anchor="nw", pady=10, padx=75)

# Ввод при нажатии клавиши Enter
window.bind("<Return>", enter_input)

# Создание экранной клавиатуры
keyboard_buttons = ["C", "<", "=", "7", "8", "9", "4", "5", "6", "1", "2", "3", "-", "0", "+"]
for i in range(len(keyboard_buttons)):
    btn = tk.Button(keyboard, text=keyboard_buttons[i], width=3, bg="black", fg="white", font=("Arial", 30),
                    command=lambda x=i: button_click(keyboard_buttons[x]))
    btn.grid(row=i//3, column=i % 3 + 1, padx=2, pady=2)
btn_ci = tk.Button(keyboard, text="C\nout", width=3, height=3, bg="black", fg="white", font=("Arial", 30),
                   command=clear_output)
btn_ca = tk.Button(keyboard, text="C\nall", width=3, height=3, bg="black", fg="white", font=("Arial", 30),
                   command=clear_all)
btn_info = tk.Button(keyboard, text="i", width=3, bg="black", fg="white", font=("Arial", 30), command=information)

btn_ci.grid(row=0, column=0, rowspan=2, padx=2, pady=2)
btn_ca.grid(row=2, column=0, rowspan=2, padx=2, pady=2)
btn_info.grid(row=4, column=0, padx=2, pady=2)

window.mainloop()