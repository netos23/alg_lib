package ru.fbtw.util;

public class SortLib {
	private static final int INSERTION_SORT_THRESHOLD = 7;

	public static <T extends Comparable<T>> void mergeSort(T[] a) {
		mergeSort(a, 0, a.length);
	}

	public static <T extends Comparable<T>> void mergeSort(T[] a, int lo, int hi) {
		T[] aux = a.clone();
		mergeSort(aux, a, lo, hi);
	}

	public static <T extends Comparable<T>> void mergeSort(T[] src, T[] target, int lo, int hi) {
		int len = hi - lo;
		if (len <= INSERTION_SORT_THRESHOLD) {
			selectionSort(target, lo, hi);
			return;
		}
		int mid = (lo + hi) >>> 1;
		mergeSort(target, src, lo, mid);
		mergeSort(target, src, mid, hi);
		if (src[mid - 1].compareTo(src[mid]) <= 0) {
			System.arraycopy(src, lo, target, lo, len);
			return;
		}

		merge(src, target, lo, hi, mid);
	}

	private static <T extends Comparable<T>> void merge(T[] src, T[] target, int lo, int hi, int mid) {
		for (int i = lo, p = lo, q = mid; i < hi; i++) {
			if (q >= hi || p < mid && src[p].compareTo(src[q]) <= 0)
				target[i] = src[p++];
			else
				target[i] = src[q++];
		}
	}

	public static <T extends Comparable<T>> void selectionSort(T[] a, int lo, int hi) {
		for (int i = lo; i < hi; i++) {
			for (int j = i; j > lo && a[j - 1].compareTo(a[j]) >= 0; j--) {
				swap(a, j - 1, j);
			}
		}
	}

	private static <T> void swap(T[] a, int i, int j) {
		T tmp = a[i];
		a[i] = a[j];
		a[j] = tmp;
	}
}
