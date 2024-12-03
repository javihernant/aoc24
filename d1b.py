import sys

def solve(path):
    sol = 0
    l = []
    r = []
    occ = {}
    with open(path) as fp:
        for line in fp:
            a, b = line.split()
            l.append(int(a))
            r.append(int(b))
    for n in r:
        if n in occ:
            occ[n]+=1
        else:
            occ[n] = 1

    for n in l:
        times = 0
        if n in occ:
            times = occ[n]
        sol += n*times

    return sol

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    sol = solve(args[0])
    print("Solution:", sol)

if __name__ == '__main__':
    main(*sys.argv[1:])
