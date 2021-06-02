from random import randint
from math_lib import mul


def gen_nums(n):
    return randint(10 ** (n - 1), 10 ** n), randint(10 ** (n - 1), 10 ** n)


def out_red(text):
    print("\033[31m{}".format(text))


def out_green(text):
    print("\033[32m{}".format(text))


def out(text):
    print("\033[37m{}".format(text))


def test(n):
    a, b = gen_nums(n)
    out('-------------------------------------------------------------------')
    print('a: %d\nb: %d\n' % (a, b))
    exp = a * b
    act = mul(a, b)

    if exp == act:
        out_green('УСПЕШНО')
    else:
        out_red('ОШИБКА')
    print('\nОжидаемый результат: %d\nФактический результат: %d\n' % (exp, act))
    out('-------------------------------------------------------------------')


if __name__ == '__main__':
    test(51)
    test(101)
    test(8)
    test(10)
    test(20)
    test(30)
