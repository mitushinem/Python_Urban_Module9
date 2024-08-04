from math import sqrt


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        i = 2
        while i <= sqrt(result):
            if result % i == 0:
                print(f'{result} - Составное число')
                break
            i += 1
        else:
            print(f'{result} - Простое число')
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


sum_three(3, 3, 5)
sum_three(2, 3, 6)
