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
    count_iter = 0
    while i >= max_num_to_multiply / 10:
        n = max_num_to_multiply
        while n >= max_num_to_multiply - count_iter:
            if is_polyndrom(i * n) and result < i * n:
                result = i * n
            n -= 1
        count_iter += 1
        i -= 1
    return result


def compute(num):
    ans = max(i * j for i in range(int(num / 10), int(num)) for j in range(int(num / 10), int(num)) if str(i * j) == str(i * j)[::-1])
    return ans


def main():
    print(compute(1000))
    print(largest_polyndrom_multiply_two_numbers(99))
    print(largest_polyndrom_multiply_two_numbers(999))
    print(largest_polyndrom_multiply_two_numbers(80))


if __name__ == '__main__':
    main()
