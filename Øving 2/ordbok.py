#!/usr/bin/python3

from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    root = Node()

    for (word,pos) in ordliste:

        word_node = root
        for i in word:

            if i not in word_node.barn:
                word_node.barn[i] = Node()

            word_node = word_node.barn[i]
        word_node.posi.append(pos)

    return root

def posisjoner(ord, indeks, node):


    if indeks  >= len(ord):
        return node.posi

    elif ord[indeks] == '?':
        pos_list = []
        for x in node.barn.values():
            pos = posisjoner(ord,indeks+1,x)
            if pos != []:
                if len(pos) > 1:
                    for y in pos:
                        pos_list.append(y)
                else:
                    pos_list.append(pos[0])
        return pos_list

    elif ord[indeks] in node.barn.keys():
        return posisjoner(ord,indeks+1,node.barn[ord[indeks]])

    else:
        return []


def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("%s:" % sokeord, end='')
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print(" %s" % p, end='')
            print()


    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()

