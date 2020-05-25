import numpy as np
from src.prim.graph_prim import Graph, tree_to_graph
from src.prim.heap import graph_to_min_heap, heap_extract_min, heap_decrease_key


def prim(G: Graph, s=0):
    """
    :param G: Graph
    :param s: starting node (index)
    :return: Minimum spanning tree (graph), sum of weights
    """
    parent = np.repeat(None, G.num_vertex)
    Q, node_id = graph_to_min_heap(G, s)
    node_in_Q = np.repeat(True, G.num_vertex)
    while len(Q):
        u = heap_extract_min(Q, node_id)
        node_in_Q[u] = False
        for v in G.vertex_map[u].adjacent:
            if node_in_Q[v] and G.vertex_map[u].weight(v) < Q[node_id[v]][1]:
                parent[v] = u
                k = G.vertex_map[u].weight(v)
                heap_decrease_key(Q, node_id[v], k, node_id)
    return tree_to_graph(parent, G)
