from sys import stdin
from random import randint

def sort_list(A):

    liste = A
    len_liste = len(liste)-1
    quick_sort(liste, 0, len_liste)
    return liste

def quick_sort(A, a, b):

    while a < b:
        p = partition(A, a, b)
        if p - a < b - p:
            quick_sort(A, a, p-1)
            a = p + 1
        else:
            quick_sort(A, p+1, b)
            b = p - 1

def partition(A, a, b):

    piv_index = randint(a, b)
    piv = A[piv_index]
    A[piv_index] = A[b]
    A[b] = piv
    i = a
    j = b - 1
    while i <= j:
        while A[i] <= piv and i <= j:
            i += 1
        while A[j] >= piv and j >= i:
            j -= 1
        if i < j:
            A[j], A[i] = A[i], A[j]

    A[b], A[i] = A[i], piv
    return i

def binarySearch_low(A, x):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2

        if x < A[mid]:
            high = mid - 1
        elif x > A[mid]:
            low = mid + 1
        else:
            return mid
    if A[mid] > x and mid != 0:
        return mid-1
    return mid

def binarySearch_high(A, x):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2

        if x < A[mid]:
            high = mid - 1
        elif x > A[mid]:
            low = mid + 1
        else:
            return mid

    if A[mid] < x and mid < len(A)-1:
        return mid+1
    return mid

def find(A, min , max):
    min_x = A[binarySearch_low(A, min)]
    max_x = A[binarySearch_high(A, max)]
    return min_x, max_x

def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))

if __name__ == "__main__":
    main()