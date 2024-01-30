import math
def binary_Search(A, n, key):
    L = 0
    R = n-1
    while L <= R :
        Mid = ((L+R)//2)
        if key == A[Mid]:
            return Mid
        elif key < A[Mid]:
            R = Mid - 1
        elif key > A[Mid]:
            L = Mid + 1
    return False

list = [84,21,47,96,15]
A = sorted(list)
n=len(A)
key = int(input("Enter the Key:"))
print(binary_Search(A, n, key))
