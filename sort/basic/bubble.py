def bubbleSort(A):
    for numElements in range(len(A), 0, -1):
        for i in range(numElements-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

def bubbleSortRec(A, n): 
    for i in range(n-1):  
        if A[i] > A[i+1]:  
            A[i], A[i+1] = A[i+1], A[i]  

    if n > 1: 
        bubbleSortRec(A, n-1)
