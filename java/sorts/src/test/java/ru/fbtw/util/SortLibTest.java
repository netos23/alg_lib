package ru.fbtw.util;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Stream;

class SortLibTest {

	public static final int MIN_LEN = 1;
	public static final int MAX_LEN = 50;

	private static Stream<Arguments> getIntArrayWorst() {
		List<Integer[]> res = new ArrayList<>();

		for (int i = MIN_LEN; i <= MAX_LEN; i++) {
			Integer[] array = IntStream.range(0, i)
					.boxed()
					.sorted(Collections.reverseOrder())
					.toArray(Integer[]::new);

			res.add(array);
		}

		return res.stream()
				.map(el -> new Object[]{el})
				.map(Arguments::of);
	}

	private static Stream<Arguments> getIntArrayBest() {
		List<Integer[]> res = new ArrayList<>();

		for (int i = MIN_LEN; i <= MAX_LEN; i++) {
			Integer[] array = IntStream.range(0, i)
					.boxed()
					.toArray(Integer[]::new);

			res.add(array);
		}

		return res.stream()
				.map(el -> new Object[]{el})
				.map(Arguments::of);
	}

	private static Stream<Arguments> getIntArrayRandom() {
		List<Integer[]> res = new ArrayList<>();
		Random random = new Random();

		for (int i = MIN_LEN; i <= MAX_LEN; i++) {
			Integer[] array = IntStream.range(0,i)
					.map(v -> random.nextInt())
					.boxed()
					.toArray(Integer[]::new);

			res.add(array);
		}

		return res.stream()
				.map(el -> new Object[]{el})
				.map(Arguments::of);
	}


	@ParameterizedTest
	@MethodSource("getIntArrayWorst")
	void mergeSortIntWorst(Integer[] arr) {
		test(arr);
	}

	@ParameterizedTest
	@MethodSource("getIntArrayBest")
	void mergeSortIntBest(Integer[] arr) {
		test(arr);
	}

	@ParameterizedTest
	@MethodSource("getIntArrayRandom")
	void mergeSortIntRandom(Integer[] arr) {
		test(arr);
	}


	private void test(Integer[] arr) {
		Integer[] copy = Arrays.copyOf(arr, arr.length);
		Arrays.sort(copy);
		SortLib.mergeSort(arr);
		Assertions.assertIterableEquals(Arrays.asList(copy), Arrays.asList(arr));
	}


}