# Implement quicksort

def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            Ai = A[i]
            Aj = A[j]
            A[i] = Aj
            A[j] = Ai
    
    A[r] = A[i+1]
    A[i+1] = x
    return i + 1

def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)   
    return A

if __name__ == "__main__":
    # Quicksort is a divide-and-conquer algorithm
    A = [4, 1, 23, 9, 1, 3]
    r = len(A)-1
    finalA = quicksort(A,0,r)

    print(finalA)