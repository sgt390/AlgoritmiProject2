import numpy as np
import time


def initialize(graph):
    min_node = np.argmin(graph[0, 1:]) + 1
    nodes = np.arange(1, len(graph[0][1:]) + 1)
    nodes = nodes[nodes != min_node]  # remove the minimum node
    return [0, min_node, 0], nodes  # circuit composed of 2 nodes


def insert(graph, cycle, k):
    # insert the node k into the cycle, minimizing the weight of the new cycle
    _min = np.inf
    for i, v in enumerate(cycle[:-1]):
        u = cycle[i+1]
        w = graph[v, k] + graph[k, u] - graph[v, u]  # always a positive value (for Triangle inequality)
        if w < _min:
            _min = w
            min_i = i+1
    cycle.insert(min_i, k)
    return cycle


def random_insert(graph, name):
    cycle, nodes = initialize(graph)
    begin = time.time()
    np.random.shuffle(nodes)  # Select phase; shuffle the nodes and then sequentially visit them
    for k in nodes:
        cycle = insert(graph, cycle, k)
    end = time.time()
    cost = sum([graph[v, u] for v, u in zip(cycle[:-1], cycle[1:])])
    print(f"Terminated: random_insert - {name}")
    return 'euristiche', name, cost, end-begin
