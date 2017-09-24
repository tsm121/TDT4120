#!/usr/bin/python3

from sys import stdin


class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0


def dfs(root):
    stack = [root, 0]
    visited = set()
    visited.add(root)
    if root.ratatosk:
        return 0

    while stack:
        node = stack.pop(0)
        level = stack.pop(0)

        for child in node.child:

            if child.ratatosk:
                return level + 1

            if child not in visited:
                visited.add(child)
                stack.append(child)
                stack.append(level + 1)

    return -1


def bfs(root):
    queue = [root, 0]

    if root.ratatosk:
        return 0

    while True:

        node = queue.pop(0)
        level = queue.pop(0)

        for child in node.child:

            if child.ratatosk:
                return level + 1
            else:
                queue.append(child)
                queue.append(level + 1)

    return -1

function = stdin.readline().strip()
number_of_nodes = int(stdin.readline())
nodes = []
for i in range(number_of_nodes):
    nodes.append(Node())
start_node = nodes[int(stdin.readline())]
ratatosk_node = nodes[int(stdin.readline())]
ratatosk_node.ratatosk = True
for line in stdin:
    number = line.split()
    temp_node = nodes[int(number.pop(0))]
    for child_number in number:
        temp_node.child.append(nodes[int(child_number)])

if function == 'dfs':
    print(dfs(start_node))
elif function == 'bfs':
    print(bfs(start_node))
elif function == 'velg':
    print(dfs(start_node))