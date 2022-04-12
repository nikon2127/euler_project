# Если выписать все натуральные числа меньше 10, кратные 3 или 5,
# то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.


def sum_of_multiples_of_3_or_5(max_num, first_mult=3, second_mult=5):
    result = 0
    i = 0
    while i < max_num:
        if (i % first_mult == 0) or (i % second_mult == 0):
            result += i
        i += 1
    return result


def main():
    print(sum_of_multiples_of_3_or_5(1000))
    print(sum_of_multiples_of_3_or_5(10000, 5, 7))


if __name__ == '__main__':
    main()
