//
// Created by nikmo on 03.06.2021.
//
#include "include/qsort.h"
#include "include/sort_utils.h"

size_t _getpvt(void *array, size_t sizeOfArray, size_t sizeOfElements, int (*cmpFunc)(const void *, const void *)) {
	switch (qsortPivot) {
		case FIRST:
			return 0;
		case LAST:
			return sizeOfArray - 1;
		case RANDOM:
			return rand() % sizeOfArray;
		case MEDIAN: {
			if ((cmpFunc(array, array + sizeOfElements * sizeOfArray / 2) > 0) !=
				(cmpFunc(array, array + sizeOfElements * (sizeOfArray - 1)) > 0)) {
				return 0;
			} else {
				if ((cmpFunc(array + sizeOfElements * sizeOfArray / 2, array) > 0) !=
					(cmpFunc(array + sizeOfElements * sizeOfArray / 2, array + sizeOfElements * (sizeOfArray - 1)) > 0))
					return sizeOfArray / 2;
				else
					return sizeOfArray - 1;
			}
		}
		default:
			printf("Неверно указан тип опорного элемента");
			exit(-1);
	}
}

size_t _prtlom(char *array, size_t sizeOfArray, size_t sizeOfElements, int (*cmpFunc)(const void *, const void *)) {
	size_t i = 0;
	swap(array + _getpvt(array, sizeOfArray, sizeOfElements, cmpFunc) * sizeOfElements, array, sizeOfElements);
	for (size_t j = 0; j < sizeOfArray; j++) {
		if (cmpFunc(array + j * sizeOfElements, array) <= 0) {
			swap(array + sizeOfElements * i++, array + j * sizeOfElements, sizeOfElements);
		}
	}
	swap(array, array + (i - 1) * sizeOfElements, sizeOfElements);
	return i - 1;
}


void qsort_l(void *array, size_t sizeOfArray, size_t sizeOfElements, int (*cmpFunc)(const void *, const void *)) {
	if (sizeOfArray <= 1) {
		return;
	}

	size_t pivot = _prtlom(array, sizeOfArray, sizeOfElements, cmpFunc);
	qsort_l(array, pivot, sizeOfElements, cmpFunc);
	qsort_l(array + (pivot + 1) * sizeOfElements, sizeOfArray - pivot - 1, sizeOfElements, cmpFunc);
}




