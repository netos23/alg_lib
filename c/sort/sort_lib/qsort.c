//
// Created by nikmo on 03.06.2021.
//

#include "include/qsort.h"

void qsortl(void *array, size_t sizeOfArray, size_t sizeOfElements, int (*cmpFunc)(const void *, const void *)) {
	if (sizeOfArray <= 1) {
		return;
	}

	size_t pivot = _prtlom(array, sizeOfArray, sizeOfElements, cmpFunc);


}

size_t _prtlom(char *array, size_t sizeOfArray, size_t sizeOfElements, int (*cmpFunc)(const void *, const void *)) {
	

}

size_t _getpvt(void *array, size_t sizeOfArray, size_t sizeOfElements, int (*cmpFunc)(const void *, const void *)) {
	switch (qsortPivot) {
		case FIRST:
			return 0;
		case LAST:
			return sizeOfArray - 1;
		case RANDOM:
			return rand() % sizeOfArray;
		case MEDIAN: {
			int cmp0l = cmpFunc(array, array + (sizeOfArray - 1) * sizeOfElements);
			int cmplm = cmpFunc(array + (sizeOfArray - 1) * sizeOfElements,
								array + sizeOfArray * sizeOfElements / 2);
			int cmp0m = cmpFunc(array + (sizeOfArray - 1) * sizeOfElements,
								array + sizeOfArray * sizeOfElements / 2);
			if (cmp0l > 0 && cmplm > 0) {
				return sizeOfArray - 1;
			} else {
				if(cmplm > )
			}
		}
		default:
			printf("Неверно указан тип опорного элемента");
			exit(-1);
	}
}

