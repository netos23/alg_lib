package ru.fbtw.util

import java.io.File
import java.util.*

fun readIntMatrix(file: File): Array<Array<Long>> {
    val sc = Scanner(file)

    val inputRows = mutableListOf<String>()
    while (sc.hasNext()) {
        inputRows.add(sc.nextLine())
    }

    return inputRows.map {
        it.split(sc.delimiter())
            .filter(String::isNotEmpty)
            .map(String::toLong)
            .toTypedArray()
    }.toTypedArray()
}

fun readInt(file: File): Long {
    val sc = Scanner(file)

    return sc.nextLong()
}