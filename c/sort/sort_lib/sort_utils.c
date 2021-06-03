//
// Created by nikmo on 03.06.2021.
//

#include <strings.h>
#include "include/sort_utils.h"

int cmpInt(void* a, void* b) {
	return *((int*) a) - *((int*) b);
}

int cmpString(void *a, void* b) {
	return strcmp((char*) a, (char*) b);
}