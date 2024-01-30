
def linear_search( A, key):
    index = 0
    while index < len(A) :

        if A[index] == key :
            return index
        else:
            index = index +1
    return -1

A = [84,21,47,96,15]

key = int(input ("Please enter key:"))

print(linear_search(A, key))


