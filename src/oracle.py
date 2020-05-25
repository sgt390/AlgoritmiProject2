def parse_oracle(file):
    names = []
    values = []
    for line in file.readlines():
        name, value = line.split()
        names.append(name)
        values.append(value)
    return names, values


def load_oracle():
    path = '../oracle.txt'
    with open(path) as f:
        names, values = parse_oracle(f)
    return list(zip(names, values))
