package ru.fbtw.math

typealias Matrix = Array<Array<Long>>

val Matrix.isSquare: Boolean
    get() = this.isNotEmpty() && this.fold(true) { acc, ints ->
        acc && ints.size == this.size
    }

fun Matrix.det(): Long {
    fun detInternal(matrix: Matrix): Long {
        if (matrix.size == 1) {
            return matrix[0][0]
        }

        if (matrix.size == 2) {
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        }

        /*if (matrix.size == 3) {
            return (matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][0] * matrix[1][2] * matrix[2][0]
                    + matrix[1][0] * matrix[2][1] * matrix[0][2] - matrix[0][2] * matrix[1][1] * matrix[2][0]
                    - matrix[0][1] * matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][1] * matrix[0][0])
        }*/

        var determinant: Long = 0
        var negCof: Long = 1
        for ((index, a) in matrix[0].withIndex()) {

            val minor = Array(matrix.size - 1) { r ->
                var col = 0
                Array(matrix.size - 1) {
                    if (col == index) col++
                    matrix[r + 1][col++]
                }
            }

            determinant += negCof * a * detInternal(minor)
            negCof *= -1
        }

        return determinant
    }

    return detInternal(this)
}
