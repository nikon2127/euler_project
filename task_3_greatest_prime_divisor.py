# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

def is_prime_num(num):
    if num <= 0:
        return False
    i = 2
    while i <= num/2:
        if num % i == 0:
            return False
        i += 1
    return True


def greatest_prime_divisor(num):
    i = 2
    while i <= num / 2:
        if num % i == 0:
            if is_prime_num(num / i):
                return int(num / i)
        i += 1
    return 1


def main():
    print(greatest_prime_divisor(13195))
    print(greatest_prime_divisor(600851475143))


if __name__ == '__main__':
    main()
