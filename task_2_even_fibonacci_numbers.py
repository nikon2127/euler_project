# Каждый следующий элемент ряда Фибоначчи получается при сложении двух
# предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи,
# которые не превышают четыре миллиона.

def sum_of_all_even_numbers_fibonacci(max_num):
    first_num = 0
    second_num = 1
    result = 0
    i = 0
    while i < max_num:
        i = first_num + second_num
        first_num = second_num
        second_num = i
        if i % 2 == 0:
            result += i
    return result


print(sum_of_all_even_numbers_fibonacci(40))
