import sys

def solve(antenas, dims):
    w, h = dims
    nodes = set()
    for ls in antenas.values():
        for i,(ai, aj) in enumerate(ls):
            for j,(bi,bj) in enumerate(ls):
                if i != j:
                    ti = ai -(bi-ai)
                    tj = aj -(bj-aj)

                    if (ti >= 0 and ti < h and tj >= 0 and tj < w):
                        nodes.add((ti,tj))
    return len(nodes)

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    antenas = dict()
    with open(args[0]) as fp:
        data = fp.read()
        data = data.splitlines()
        h = len(data)
        w = len(data[0])
        for i,line in enumerate(data):
            for j, ch in enumerate(line):
                if ch != '.':
                    if ch not in antenas:
                        antenas[ch] = [(i,j)]
                    else:
                        antenas[ch].append((i,j))
        sol = solve(antenas,(w,h))
        print("Solution:", sol)

def test():
    op_rec([2,3], 0, 3, 1)
    

if __name__ == '__main__':
    #test()
    main(*sys.argv[1:])
