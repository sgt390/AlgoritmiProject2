import os
import numpy as np


def parse_header(file):
    header = {}
    while file.readable():
        line = file.readline()
        if line.startswith('NODE_COORD_SECTION'):
            break
        title, value = line.rstrip().split(':')
        header[title.rstrip(':').strip()] = value.strip()
    return header


def parse_input(file):
    header = parse_header(file)
    nodes = []
    longitude = np.array([])
    latitude = np.array([])
    while file.readable():
        line = file.readline().strip()
        if line.startswith('EOF'):
            break
        node, x, y = map(float, line.split())
        nodes.append(int(node-1))
        longitude = np.append(longitude, y)
        latitude = np.append(latitude, x)
    return (nodes, longitude, latitude, header['EDGE_WEIGHT_TYPE']), header['NAME']


def load_inputs():
    inputs = []
    root = '../tsp_dataset/'
    for path in os.listdir(root):
        with open(root + path) as f:
            inputs.append(parse_input(f))
    return inputs
