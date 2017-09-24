
def binSearch(A, low, high, x):

    if low > high:
        return ""

    mid = int(low + (high - low) / 2)
    print(A[low:high])
    print("Low: " + str(A[low]) + " High: " + str(A[high]) + " Mid: " + str(A[mid]) + " Find: " + str(x))

    if x == A[mid]:
        print("FOUND " + str(x))
        return A[mid]

    elif x < A[mid]:
        return binSearch(A, low, mid-1, x)

    elif x > A[mid]:
        return  binSearch(A, mid+1, high, x)



def binary_search(A,x):
    high = len(A)-1
    low = 0

    best_ind = low

    while low <= high:
        mid = low + (high - low) // 2

        if x > A[mid]:
            low = mid + 1
        elif x < A[mid]:
            high = mid-1
        else:
            best_ind = mid
            break

        if abs(A[mid] - x) < abs(A[best_ind] - x):
            print(A[mid],A[best_ind])
            print(str(abs(A[mid])) + " < " + str(abs(A[best_ind])))
            print(best_ind)
            best_ind = mid
    return best_ind


A = [2,4,16,43,66,90,132]

x = binary_search(A,15)
print(A[x])

