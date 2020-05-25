import numpy as np
import math

# source for rad, distance_rad: http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/TSPFAQ.html
PI = 3.141592
RRR = 6378.388


def rad(x):
    deg = int(x)
    _min = x - deg
    _rad = PI * (deg + 5.0 * _min / 3.0) / 180.0
    return _rad


def distance_rad(longitude, latitude):
    q1 = math.cos(longitude[0] - longitude[1])
    q2 = math.cos(latitude[0] - latitude[1])
    q3 = math.cos(latitude[0] + latitude[1])
    dij = int(RRR * math.acos(0.5 * ((1.0+q1) * q2 - (1.0-q1) * q3)) + 1.0)
    return dij


def distance_euc(lon1, lat1, lon2, lat2):
    q1 = lon1 - lon2
    q2 = lat1 - lat2
    return round(math.sqrt(q1**2 + q2**2))


def make_graph(inp):
    nodes, longitude, latitude, weight_type = inp
    dim = len(nodes)
    w = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(i):  # cycle only the lower triangular part of the adjacency matrix
            if weight_type == 'GEO':
                lon = [rad(longitude[i]), rad(longitude[j])]
                lat = [rad(latitude[i]), rad(latitude[j])]
                w[i, j] = distance_rad(lon, lat)
            elif weight_type == 'EUC_2D':
                w[i, j] = distance_euc(longitude[i], latitude[i], longitude[j], latitude[j])
            w[j, i] = w[i, j]
    return w
