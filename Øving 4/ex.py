def binarySearch(A, x):
    low, high = 0, len(A) - 1
    best_ind = low
    while low <= high:
        mid = low + (high - low) // 2
        if A[mid] < x:
            low = mid + 1
        elif A[mid] > x:
            high = mid - 1
        else:
            best_ind = mid
            break
        # check if A[mid] is closer to val than A[best_ind]
        if abs(A[mid] - x) < abs(A[best_ind] - x):
            best_ind = mid
    return best_ind

#def main():
#    data = [1, 2, 3, 4, 5, 6, 7]
#    val = 6.1
#    ind = binarySearch(data, val)
#    print ('data[%d]=%d' % (ind, data[ind]))

#if __name__ == '__main__':
#    main()

A = [2,4,16,43,66,90,132]

x = binarySearch(A,15)
print(x)
