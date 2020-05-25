from src.oracle import load_oracle
from collections import defaultdict
import pandas as pd


def get_oracle():
    dict_oracle = dict(load_oracle())
    return dict_oracle


def organize(results):
    grp_res = defaultdict(lambda: {})
    res = []
    algs = []
    for alg, file, weight, time, error in results:
        grp_res[file][alg] = [int(weight), round(time, 5), round(error, 6)]
        if alg not in algs:
            algs.append(alg)
    for file in grp_res:
        x = [file] + grp_res[file][algs[0]]
        for alg in algs[1:]:
            x.extend(grp_res[file][alg])
        res.append(x)
    return res


def to_str(table):
    table = list(map(lambda row: list(map(str, row)), table))
    str_res = f"{''.join(['-' for _ in range(114)])}\n"
    str_res += f"{' ':^14}|{'Held Karp':^32}|{'Random':^32}|{'TSP':^32}\n"
    str_res += f"{''.join(['-' for _ in range(114)])}\n"
    for x in table:
        str_res += f"{x[0]:^14}|{x[1]:^10} {x[2]:^10} {x[3]:^10}|{x[4]:^10} {x[5]:^10} {x[6]:^10}|{x[7]:^10} {x[8]:^10} {x[9]:^10}\n"
        str_res += f"{''.join(['-' for _ in range(114)])}\n"
    return str_res


def make_results(results):
    algs = []
    files = []
    weights = []
    times = []
    errors = []
    oracle = get_oracle()
    for algorithm, name, weight, time in results:
        delta_weight = float(weight) - float(oracle[name.split('.')[0]+'.tsp'])
        error = delta_weight / weight
        algs.append(algorithm)
        files.append(name)
        weights.append(weight)
        times.append(time)
        errors.append(error)
    zipped_list = list(zip(algs, files, weights, times, errors))
    org = organize(zipped_list)
    table = pd.DataFrame(org, columns=['Name', 'Result', 'Time', 'Error', 'Result', 'Time', 'Error', 'Result', 'Time', 'Error'])
    with open('../result.md', 'w+') as f:
        f.write(to_str(org))
    return table
