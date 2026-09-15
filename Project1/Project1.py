def HybridMergeSort(A, left, right, S):
    size = right - left + 1
    if size <= S:
        InsertionSort(A, left, right)
    else:
        mid = (left + right) // 2
        # recursive calls for MergeSort
        HybridMergeSort(A, left, mid, S)
        HybridMergeSort(A, mid + 1, right, S)

        Merge(A, left, mid, right)

def InsertionSort(A, left, right):
    for i in range(left+1, right+1): # python does not include last value, so want right to be included
        key = A[i]
        j = i-1
        while j >= left and A[j] > key: # checking if the value is bigger than the one before it
            A[j + 1] = A[j]
            j -= 1 # shifting j to the right

        A[j + 1] = key

def Merge(A, left, mid, right):
    # python slicing 
    L = A[left:mid+1]
    R = A[mid+1:right+1]
    i = j = 0  # initialise starting pointers
    k = left # starting point
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

        k += 1

    # filling in remaining elements
    # Copy anything remaining in L
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    # Copy anything remaining in R
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1