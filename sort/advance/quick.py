def quickSort(A, p:int, r:int): 
    if p < r:
        q = partition(A, p, r) 
        quickSort(A, p, q)
        quickSort(A, q+1, r) 
def partition(A, p:int, r:int) -> int:
    x = A[p]  
    i = p - 1 
    j = r + 1  
    while True:
        i += 1 
        while A[i] < x: 
            i += 1
        j -= 1 
        while A[j] > x: 
            j -= 1
        if i >= j: 
            return j 
        A[i], A[j] = A[j], A[i] 

def quickSortEqual(A, p:int, r:int):
    if p < r:
        q = partition2(A, p, r)
        quickSortEqual(A, p, q-1)
        quickSortEqual(A, q+1, r)

def partition2(A, p:int, r:int) -> int:
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
        elif A[j] == x:
            if j % 2 == 0:
                i += 1
            else:
                i += 1
                A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quickSortPython(array):
    if len(array) <= 1:
        return array
    pivot, tail = array[0], array[1:]
    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]
    return quickSortPython(leftSide) + [pivot] + quickSortPython(rightSide)
