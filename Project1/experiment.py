import random
from hybrid_sort import HybridMergeSort

# # generating the data
# def generate_data(n, x):
#     A = [] # start with empty list
#     for _ in range(n):
#         A.append(random.randint(1, x))
#     return A

# # number of data to be iterated
# n_values = [1000, 10000, 100000, 1000000, 10000000]
# # range of values
# x = 1000 
# # threshold value
# S = 2
# for n in n_values:
#     A = generate_data(n, x)

# test on small array
A = [4, 5, 9, 0, 8, 2, 6, 1, 7, 3]
S = 2
comparisons = HybridMergeSort(A, 0, len(A) - 1, S)


print(A)
# print("n =", n, "length =", len(A))
print("Key comparisons:", comparisons)
