#!/usr/bin/python3

from sys import stdin

def flexradix3(A, d):
    print("List: " + str(A))
    int_list = []
    max_element = 0

    for word_index in range(len(A)):
        if len(A[word_index]) <= d:
            #print ("Str: " + A[word_index])
            word_list = []

            for ltr_index in range(len(A[word_index])):
                letter = ord(A[word_index][ltr_index])-96
                word_list.append(letter)

                if letter > max_element:
                    max_element = letter

            while(len(word_list) < 6):
                word_list.append(0)
            int_list.append(word_list)

    print("Int list:",int_list)
    print(max_element)
    compare(int_list, 0, max_element)

def compare(A, index, max_element):
    list = [[] for _ in range(max_element)]
    i = index

    for x in range(len(A)):
        letter = A[x][i]
        list[letter].append(letter)
    print(list)

def flexradix(A, d):
    L = []

    for x in A:
        if len(x) <= d:
            L.append(x)

    return radix_sort(L,0)

def radix_sort(A, i):

    if len(A) <= 1:
        return A

    sorted_bucket = []
    buckets = [[] for j in range(27)]

    for word in A:
        if i >= len(word):
            sorted_bucket.append(word)
        else:
            buckets[ord(word[i]) - 97].append(word)

    new_list = []

    for x in buckets:

        if len(x) > 0:

            t = radix_sort(x, i + 1)
            if t is not None:
                new_list.append(t)
                buckets = new_list
    a = []
    for b in buckets:
        for e in b:
            a.append(e)

    print(a)
    return a

    #buckets = [radix_sort(b, i + 1) for b in buckets if len(b) > 0]


    #return sorted_bucket + [element for b in buckets for element in b]

def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, d)
    print("\nMAIN")
    for string in A:
        print(string)

if __name__ == "__main__":
    main()