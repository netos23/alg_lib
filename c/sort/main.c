#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "sort_lib/include/qsort.h"
#include "sort_lib/include/sort_utils.h"

int main() {
	srand(time(0));
	int ar[20];
	for (int i = 19; i >= 0; i--) {
		ar[20 - i - 1] = i;
	}
	qsort_l(ar, 20, sizeof(int), cmpInt);

	for (int i = 0; i < 20; i++) {
		printf("%d ", ar[i]);
	}
	return 0;
}
