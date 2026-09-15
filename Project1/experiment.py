from hybrid_sort import HybridMergeSort

A = [7, 4, 5, 2, 8, 1, 6, 3]
S = 2

comparisons = HybridMergeSort(A, 0, len(A) - 1, S)

print(A)
print(comparisons)