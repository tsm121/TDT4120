from sys import stdin, stderr

Inf = float('Inf')

class Node:

    def __init__(self):
        self.d = Inf
        self.e = [] #Neighbours

def best_path(nm, prob):
    s = []
    q = make_graph(nm, prob)
    nodes = q.copy()
    path = [nodes[0].d]


    while True:
        u, q = extract_max(q)
        path.append(u.d)
        if u == nodes[-1]:
            break

    print(path)


def extract_max(q):
    maximum = -9999

    node_max = None

    for v in q:
        if v.d > maximum:
            maximum = v.d
            node_max = v

    q.remove(node_max)

    return node_max, q




def best_path2(nm, prob):
    graph = make_graph(nm, prob)
    temp = -9999
    temp_neighbour = -1
    path = [0]

    for i in range(len(graph)):
        vertex = graph[i].e

        for neighbour in vertex:
            print("Vertex nr: ", i)
            print("e.d", graph[neighbour].d, " > ", "temp", temp)
            if graph[neighbour].d > temp:
                temp = graph[neighbour].d
                temp_neighbour = neighbour
                path.append(neighbour)

    #todo: slette self_node i besøkt nabo-node
    p#rint(path)


    return 0


def make_graph(nm, prob):
    #counter = 0
    num_nodes = len(nm)
    graph = [Node() for x in range(num_nodes)]

    for i in range(num_nodes):
        #counter += 1
        graph[i].d = prob[i]
        j = num_nodes - 1

        while j > i:
            #counter += 1
            if nm[i][j] == 1:
                graph[i].e.append(j)
                graph[j].e.append(i)

            j -= 1

    #for v in graph:
    #    print("Prob: ", v.d, " Neighbours: ", v.e)

    #print("Counter", counter)

    return graph



n = int(stdin.readline())
probabilities = [float(x) for x in stdin.readline().split()]
neighbour_matrix = []
for line in stdin:
    neighbour_row = [0] * n
    neighbours = [int(neighbour) for neighbour in line.split()]
    for neighbour in neighbours:
        neighbour_row[neighbour] = 1
    neighbour_matrix.append(neighbour_row)
print (best_path(neighbour_matrix, probabilities))