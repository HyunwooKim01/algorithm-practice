def selectionSort(A):
    for last in range(len(A)-1, 0, -1):
        k = theLargest(A, last)
        A[k], A[last] = A[last], A[k]

def theLargest(A, last:int) -> int:
    largest = 0
    for i in range(last+1):
        if A[i] > A[largest]:
            largest = 1
    return largest

def selectionSortRec(A, n): 
    if n >= 1:  
        k = theLargest4Rec(A, n)
        A[k], A[n-1] = A[n-1], A[k]  
        selectionSortRec(A, n-1)

def theLargest4Rec(A, last:int) -> int:
    largest = last - 1  
    for i in range(last-1): 
        if A[i] > A[largest]:
            largest = i
    return largest
