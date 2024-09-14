# Автор программы: Сойников Павел, ИУ7-24Б
# Назначение программы: в данном модуле содержатся все функции для имитации работы восьмиразрядного сумматора:
# перевод из десятичной системы в двоичную и наоборот, создание доп кода, сумма двух чисел в бинарном виде
# (с учетом переполнения)

# Перевод целого числа из десятичной системы в двоичную
def dec_to_bin(dec_number):
    number = abs(dec_number)
    bin_number = ""
    rest_part = number
    while rest_part > 0:
        bin_number = str(rest_part % 2) + bin_number
        rest_part = rest_part // 2

    if len(bin_number) > 7:
        return "-"
    if len(bin_number) < 7:
        bin_number = "0" * (7 - len(bin_number)) + bin_number
    if dec_number < 0:
        bin_number = "1" + bin_number
    if dec_number >= 0:
        bin_number = "0" + bin_number
    return bin_number


# Перевод целого числа из двоичной системы в десятичную
def bin_to_dec(bin_number):
    if bin_number == "-":
        return "-"

    dec_number = 0
    cnt = 0
    for i in range(len(bin_number)-1, 0, -1):
        if bin_number[i] == "1":
            dec_number += 2**cnt
        cnt += 1
    if bin_number[0] == "1":
        dec_number *= -1
    return dec_number


# Образование дополнительного кода числа
def bonus_code(bin_number):
    if bin_number == "-":
        return bin_number

    if bin_number[0] == "0":
        return bin_number
    reversed_bin_number = ""
    for i in range(1, len(bin_number)):
        if bin_number[i] == "0":
            reversed_bin_number += "1"
        else:
            reversed_bin_number += "0"
    bin_number = reversed_bin_number

    sum_elem = "1"
    sum_res = ""
    k = len(bin_number) - 1
    while k >= 0:
        if sum_elem == "1" and bin_number[k] == "0":
            sum_res = "1" + sum_res
            sum_elem = "0"
        elif sum_elem == "1" and bin_number[k] == "1":
            sum_res = "0" + sum_res
            sum_elem = "1"
        elif sum_elem == "0":
            sum_res = bin_number[k] + sum_res
            sum_elem = "0"
        if sum_elem == "1" and k == 0:
            sum_res = "-"
        k -= 1
    sum_res = "1" + sum_res
    bin_number = sum_res
    return bin_number


# Сумма двух бинарных чисел
def bin_sum(bin_number, sum_elem):
    if bin_number == "-" or sum_elem == "-":  # Невалидные данные
        return "-"

    sum_res = ""
    prev_sum = "0"
    overflow = False
    k = 7  # Число разрядов (1 разряд из 8 - знаковый)
    while k >= 0:
        if (sum_elem[k] == "1" and bin_number[k] == "0") or (sum_elem[k] == "0" and bin_number[k] == "1"):
            if prev_sum == "0":
                sum_res = "1" + sum_res
            elif prev_sum == "1":
                sum_res = "0" + sum_res
        elif sum_elem[k] == "1" and bin_number[k] == "1":
            if prev_sum == "0":
                sum_res = "0" + sum_res
                if k == 0:
                    overflow = True
                prev_sum = "1"
            elif prev_sum == "1":
                sum_res = "1" + sum_res
        elif sum_elem[k] == "0" and bin_number[k] == "0":
            if prev_sum == "0":
                sum_res = "0" + sum_res
            elif prev_sum == "1":
                if k == 0:
                    overflow = True
                sum_res = "1" + sum_res
                prev_sum = "0"
        k -= 1

    # print(sum_res)
    # print(prev_sum)

    if overflow or sum_res == "10000000":  # Переполнение
        return "-"

    return sum_res


# Восьмиразрядный сумматор
def summator(a, b):

    # Исходные числа в доп коды
    bin_number = bonus_code(dec_to_bin(a))
    sum_elem = bonus_code(dec_to_bin(b))

    # Сумма доп кодов (с учетом переполнения)
    summ = bin_sum(bin_number, sum_elem)

    # Доп код полученной суммы
    res_bin = bonus_code(summ)

    # Перевод в десятичную
    res = bin_to_dec(res_bin)

    return res