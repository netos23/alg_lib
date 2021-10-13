import functools
import math
from sympy import *

n = symbols('n')


def compare_fun(a, b):
	f = a / b
	cmp = limit(f, n, math.inf)
	if cmp == 0:
		return -1
	elif cmp == math.inf:
		return 1
	else:
		print('Растут с одинаковой скоростью: ')
		pprint(a)
		print()
		print()
		pprint(b)
		print('----------------------------')
		return -1 if cmp < 1 else 0 if cmp == 1 else 1


if __name__ == '__main__':
	init_printing(use_unicode=False)
	funcs = [
		(sqrt(2)) ** log(n, 2),  # sqrt(n)
		n ** 2,
		factorial(n),
		factorial(log(n, 2)),
		(3 / 2) ** n,
		n ** 3,
		(log(n, 2)) ** 2,
		log(factorial(n)) / log(2),
		2 ** (2 ** n),
		n ** (1 / log(n, 2)),  # 2
		log(log(n)),
		n * (2 ** n),
		n ** (log(log(n, 2), 2)),
		log(n),
		1,
		2 ** log(n, 2),  # n
		(log(n, 2)) ** log(n, 2),
		math.e ** n,
		(2 ** n) * factorial(n),
		sqrt(log(n, 2)),
		2 ** sqrt(2 * log(n, 2)),
		n * log(n, 2),
		2 ** n,
		n
	]
	funcs.sort(key=functools.cmp_to_key(compare_fun))
	print('Отсортированные функции')
	for fun in funcs:
		print('--------------------------\n')
		pprint(fun)
		print('\n--------------------------')
