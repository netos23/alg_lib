cmake_minimum_required(VERSION 3.17)
project(sort C)

set(CMAKE_C_STANDARD 99)

add_executable(sort main.c sort_lib/qsort.c sort_lib/include/qsort.h sort_lib/sort_utils.c sort_lib/include/sort_utils.h)