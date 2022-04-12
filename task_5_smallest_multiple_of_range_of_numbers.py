# 2520 самое маленькое число, которое делится нацело на все числа от 1 до 10
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

def smallest_multiple_of_range(start, end):
    result = 2
    while True:
        i = start
        while i <= end:
            if result % i != 0:
                break
            if i == end:
                return result
            i += 1
        result += 2


def main():
    print(smallest_multiple_of_range(1, 10))
    print(smallest_multiple_of_range(1, 15))
    print(smallest_multiple_of_range(1, 20))


if __name__ == '__main__':
    main()
