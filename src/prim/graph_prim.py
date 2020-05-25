import numpy as np


class Vertex:
    def __init__(self, name):
        self.id = name
        self.adjacent = {}  # typed.Dict.empty(types.int64, types.int64)
        self.visited = 0

    def add_neighbor(self, v, weight):
        # if v in self.adjacent and self.adjacent[v] < weight:
        #    weight = self.adjacent[v]
        self.adjacent[v] = weight

    def weight(self, v):
        return self.adjacent[v]


class Edge:
    def __init__(self, id_, u, v, weight):
        self.id = id_
        self.u = u
        self.v = v
        self.weight = weight

    def flatten(self):
        return self.u, self.v, self.weight


def edge_id(u, v):
    u, v = sorted([v, u])
    return int(0.5 * (u + v) * (u + v + 1) + v)


class Graph:
    def __init__(self, matrix=(), num_v=0):
        self.num_vertex = 0
        self.vertex_map = np.repeat(None, num_v)
        self.is_vertex = np.repeat(False, num_v)
        self.edges = {}
        self.incident_edges = np.repeat({}, num_v)
        self.neighbors = [[] for _ in range(int(num_v))]
        for (v, u, weight) in matrix:
            self.add_edge(v, u, weight)

    def add_vertex(self, node):
        if not self.is_vertex[node]:
            self.is_vertex[node] = True
            self.num_vertex += 1
            self.vertex_map[node] = Vertex(node)
            self.incident_edges[node] = set()
        return self.vertex_map[node]

    def add_edge(self, v, u, weight):
        self.add_vertex(v)
        self.add_vertex(u)
        self.vertex_map[v].add_neighbor(u, weight)
        self.vertex_map[u].add_neighbor(v, weight)
        e_id = edge_id(u, v)
        edge = Edge(e_id, u, v, weight)
        self.edges[e_id] = edge
        self.incident_edges[v].add(edge)
        self.incident_edges[u].add(edge)
        self.neighbors[v].append(u)
        self.neighbors[u].append(v)


def tree_to_graph(t, G):  # O(|t|)
    mst = Graph((), G.num_vertex)
    for i, adj in enumerate(t):
        mst.add_vertex(i)
        if adj is not None:
            w = G.vertex_map[adj].weight(i)
            mst.add_edge(i, adj, w)
    return mst


def from_adj(adj):
    # from adjacency matrix to instance of Graph
    g = Graph(num_v=adj.shape[0])
    for v in range(adj.shape[0]):
        for u in range(v):
            g.add_edge(v, u, adj[v, u])
    return g
