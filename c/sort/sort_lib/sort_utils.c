//
// Created by nikmo on 03.06.2021.
//

#include <strings.h>
#include "include/sort_utils.h"

int cmpInt(const void *a, const void *b) {
	return *((int *) a) - *((int *) b);
}

int cmpString(const void *a, const void *b) {
	return strcmp((char *) a, (char *) b);
}

void swap(void *a, void *b, size_t size) {
	void *tmp = malloc(size);
	memcpy(tmp, a, size);
	memcpy(a, b, size);
	memcpy(b, tmp, size);

	free(tmp);
}