from math_lib import mul

if __name__ == '__main__':
    print('Введите два числа:')
    f, s = int(input('>')), int(input('>'))
    exp = f * s
    act = mul(f, s)
    print('Ожидаемый результат: %d\nФактический результат: %d' % (exp, act))
