import sys

def run_check(els, n, acc, val):
    if n == 0:
        return acc == val

    a = run_check(els[1:], n-1, els[0] + acc, val)
    if a:
        return True
    b= run_check(els[1:], n-1, els[0] * acc, val)
    if b:
        return True
    tmp = int(str(acc) + str(els[0]))
    c= run_check(els[1:], n-1, tmp, val)
    if c:
        return True
    return False

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    sol = 0
    with open(args[0]) as fp:
        data = fp.read()
        for line in data.splitlines():
            val, els = line.split(": ")
            val = int(val)
            els = els.split(" ")
            els = [int(e) for e in els]
            if (run_check(els[1:], len(els)-1, els[0], val)):
                sol += val

    print("Solution:", sol)

def test():
    op_rec([2,3], 0, 3, 1)
    

if __name__ == '__main__':
    #test()
    main(*sys.argv[1:])
