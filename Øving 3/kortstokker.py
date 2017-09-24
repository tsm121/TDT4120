#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    while len(decks) > 1:
        L = decks[0]
        R = decks[-1]
        decks[0] = merge2(L,R)
        decks.remove((decks[-1]))
    return ''.join(x[1] for x in decks[0])

def merge2(L,R):
    length = len(L) + len(R)
    inf = float("inf")
    end = (inf, )
    L.append(end)
    R.append(end)
    newL = []
    p = 0
    r = 0
    while len(newL) < length:
        if L[p][0] > R[r][0]:
            newL.append(R[r])
            r += 1
        else:
            newL.append(L[p])
            p += 1
    return newL

def main():
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    print(merge(decks))

if __name__ == "__main__":
    main()