# Число-палиндром с обеих сторон (справа налево и слева направо)
# читается одинаково. Самое большое число-палиндром, полученное умножением
# двух двузначных чисел – 9009 = 91 × 99. Найдите самый большой палиндром,
# полученный умножением двух трехзначных чисел.

def is_polyndrom(num):
    if int(str(num)[::-1]) == num:
        return True
    return False


def largest_polyndrom_multiply_two_numbers(max_num_to_multiply):
    result = 0
    i = max_num_to_multiply
    while i >= 1:
        n = max_num_to_multiply
        while n >= 1:
            result = i * n
            if is_polyndrom(result):
                return result
            n -= 1
        i -= 1
    return 0


print(largest_polyndrom_multiply_two_numbers(99))
print(largest_polyndrom_multiply_two_numbers(999))
print(largest_polyndrom_multiply_two_numbers(80))
