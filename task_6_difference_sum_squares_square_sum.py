# Сумма квадратов первых десяти натуральных чисел равна
# 1**2 + 2**2 + ... + 10**2 = 385
# Квадрат суммы первых десяти натуральных чисел равен
# (1 + 2 + ... + 10)**2 = 55**2 = 3025
# Следовательно, разность между суммой квадратов и квадратом суммы первых
# десяти натуральных чисел составляет 3025 − 385 = 2640.
# Найдите разность между суммой квадратов и квадратом суммы первых
# ста натуральных чисел.

def difference_sum_squares_square_sum(num):
    sum_squares = 0
    square_sum = 0
    for i in range(1, num + 1):
        sum_squares += i ** 2
        square_sum += i
    return square_sum ** 2 - sum_squares


def main():
    print(difference_sum_squares_square_sum(10))
    print(difference_sum_squares_square_sum(20))
    print(difference_sum_squares_square_sum(100))
    print(difference_sum_squares_square_sum(1000))


if __name__ == '__main__':
    main()
