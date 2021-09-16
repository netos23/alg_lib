package ru.fbtw.math

import org.junit.jupiter.api.Assertions
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.MethodSource
import ru.fbtw.util.readInt
import ru.fbtw.util.readIntMatrix
import java.io.File
import java.util.stream.Stream

internal class MatrixDetTest {

    @ParameterizedTest
    @MethodSource("getInput")
    fun det(test: Pair<Matrix, Long>) {
        val (matrix, answer) = test
        Assertions.assertEquals(answer, matrix.det())
    }


    companion object {
        @JvmStatic
        val inputSize = arrayOf(3,10)

        const val inputPath = "./inputs/input"


        const val outputPath = "./outputs/output"

        const val filenameSuffix = ".txt"

        @JvmStatic
        fun getInput(): Stream<Pair<Matrix, Long>> {
            val args = mutableListOf<Pair<Matrix, Long>>()
            for(size in inputSize){
                val inpPath = "$inputPath$size$filenameSuffix"
                val inpFile = File(inpPath)


                val outPath = "$outputPath$size$filenameSuffix"
                val outFile = File(outPath)

                val matrix = readIntMatrix(inpFile)
                val answer = readInt(outFile)

                args.add(matrix to answer)
            }

            return args.stream()
        }
    }
}