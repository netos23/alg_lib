# Функция для определения длины числа
def len_i(n):
    return len(str(n))


# Функция разбиения числа
def split_num(num, m):
    return num // m, num % m


def mul(first, second):
    # Определяем длину числа
    len_f = len_i(first)
    len_s = len_i(second)

    # Если одна из длин равна еденицы то производим умножение
    if len_f == 1 or len_s == 1:
        return first * second
    else:
        # Определяем опорную длину, для случаев с разными длинами
        n = min(len_f, len_s)
        half_n = n // 2
        m = 10 ** half_n

        a, b = split_num(first, m)
        c, d = split_num(second, m)

        ac = mul(a, c)
        bd = mul(b, d)
        mid = mul(a + b, c + d)

        return (ac * 10 ** (half_n * 2)) + ((mid - ac - bd) * 10 ** half_n) + bd
