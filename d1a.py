import sys

def solve(path):
    sol = 0
    l = []
    r = []
    with open(path) as fp:
        for line in fp:
            a, b = line.split()
            l.append(int(a))
            r.append(int(b))
    l.sort()
    r.sort()
    for i in range(len(l)):
        sol += abs(l[i] - r[i])
    return sol

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    sol = solve(args[0])
    print("Solution:", sol)

if __name__ == '__main__':
    main(*sys.argv[1:])
