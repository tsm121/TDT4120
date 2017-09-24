#!/usr/bin/python3

from sys import stdin

def flexradix(A, d):
    L = []
    #Sjekker om ord er <= d
    for x in A:
        if len(x) <= d:
            L.append(x)

    return radix_sort(L,0)

def radix_sort(A, i):
    #Base case. Stopper om det bare er ett element igjen
    if len(A) <= 1:
        return A

    sorted_bucket = []
    buckets = [[] for j in range(27)] #Lager bucket for alle bokstaver a-z

    #Sorterer ord i buckets
    for word in A:
        if i >= len(word):
            sorted_bucket.append(word)
        else:
            # Legger til ord i bucket. Ser på ASCII-verdien til i-te bokstav
            buckets[ord(word[i]) - 97].append(word)

    new_list = []
    #Går igjennom buckets
    for x in buckets:
        #Unngår tomme buckets
        if len(x) > 0:
            #Sorterer buckets igjen for å sjekke i-te bokstav
            t = radix_sort(x, i + 1)
            #Unngår tomme buckets
            if t is not None:
                new_list.append(t)
                buckets = new_list
    """
    a = []
    for b in buckets:
        for e in b:
            a.append(e)

    return a
    """
    #Fjerner liste i liste og returnerer sortert liste
    return sorted_bucket + [b for L in buckets for b in L]

def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, d)
    for string in A:
        print(string)

if __name__ == "__main__":
    main()