import numpy as np
from threading import Timer
import time
import sys
global timeout

sys.setrecursionlimit(10**6)  # more recursive calls are required


def time_limit():  # if timeout is true, the recursive calls will terminate
    global timeout
    timeout = True


def hk_visit(v, S, d, weight):
    global timeout
    if S == {v}:
        return weight[v, 0]
    elif (v, S) in d:
        return d[(v, S)]
    else:
        mindist = np.inf
        for u in S.difference({v}):  # find the min_dist w.r.t. each remaining node
            dist = hk_visit(u, S.difference({v}), d, weight)  # approximated if the time limit is reached
            if dist + weight[u, v] < mindist:
                mindist = dist + weight[u, v]
            if timeout:
                break  # approximated result, the check is here to avoid mindist = inf
        d[(v, S)] = mindist
        return mindist


def hs_tsp(graph, name):
    global timeout
    timeout = False
    t = Timer(180, time_limit)  # after 180s, time_limit wakes up and stops the execution
    begin = time.time()
    d = dict()
    t.start()
    # a frozenset can be used as list index
    res = hk_visit(0, frozenset(range(graph.shape[1])), d, graph)
    t.cancel()
    end = time.time()
    print(f"Terminated: held karp - {name}")
    return 'held karp', name, res, end-begin
