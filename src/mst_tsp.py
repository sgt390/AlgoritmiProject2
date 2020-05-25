import numpy as np
from src.prim.graph_prim import from_adj
from src.prim.prim import prim
import time


def preorder(T, v, visited=np.array([])):
    # Instance of graph T into a list of nodes, visited in preorder starting from node v
    # visited array keeps track of visited nodes
    p = []
    if v in visited:
        return []
    for u in T.neighbors[v]:
        p += preorder(T, u, np.append(visited, v))
    return [v] + p


def approx_tsp(G):
    V = range(G.num_vertex)
    r = V[0]
    T = prim(G, r)
    hp = preorder(T, r)
    return np.append(hp, hp[0])


def mst_tsp(adj, name):
    begin = time.time()
    g = from_adj(adj)
    pre = approx_tsp(g)
    end = time.time()
    cost = sum([adj[x, pre[i+1]] for i, x in enumerate(pre[:-1])])
    print(f"Terminated: mst tsp - {name}")
    return 'mst_tsp', name, cost, end - begin
