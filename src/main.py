from src import graph, inputs, heldkarp, results, euristiche, mst_tsp
from concurrent.futures import ThreadPoolExecutor

input_graphs = inputs.load_inputs()
graphs = []
names = []


for g, info in input_graphs:
    name = info
    graphs.append(graph.make_graph(g))
    names.append(name)


params_hk = [(heldkarp.hs_tsp, graph, name) for graph, name in zip(graphs, names)]
params = [(euristiche.random_insert, graph, name) for graph, name in zip(graphs, names)]
params += [(mst_tsp.mst_tsp, graph, name) for graph, name in zip(graphs, names)]

if __name__ == '__main__':
    futures = []
    result = []

    # Held Karp requires a separate execution because it requires a lot of memory and computational power
    with ThreadPoolExecutor() as executor:
        for alg, graph, name in params_hk:
            futures.append(executor.submit(alg, graph, name))

    for f in futures:
        result.append(f.result())

    # Execute random insert and mst_tsp concurrently
    futures = []
    with ThreadPoolExecutor() as executor:
        for alg, graph, name in params:
            futures.append(executor.submit(alg, graph, name))

    for f in futures:
        result.append(f.result())

    print(results.make_results(result))
