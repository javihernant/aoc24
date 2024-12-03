import sys

def is_safe(ls):
    if (len(ls)==1):
        return True
    diff = ls[1] - ls[0]
    if (diff > 0):
        i = 1
        while (i<len(ls)):
            diff = ls[i] - ls[i-1]
            if (not (diff > 0 and diff <= 3)):
                return False
            i+=1
    elif (diff < 0):
        i = 1
        while (i<len(ls)):
            diff = ls[i] - ls[i-1]
            if (not (diff < 0 and diff >= -3)):
                return False
            i+=1
    else:
        return False
    return True


def solve(path):
    sol = 0
    with open(path) as fp:
        for line in fp:
            ls = line.split()
            ls = [int(e) for e in ls]
            if (is_safe(ls)):
                sol +=1
    return sol

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    sol = solve(args[0])
    print("Solution:", sol)

if __name__ == '__main__':
    main(*sys.argv[1:])
