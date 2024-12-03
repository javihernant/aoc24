import sys

def pos_after_mul(line):
    if (len(line) < 8):
        return (0, 1,-1,-1)
    if (line[0:4] == 'mul('):
        i=4
        a=''
        b=''
        while (i<len(line)):
            if (line[i] == ','):
                if (len(a)==0):
                    return (0, i+1, -1,-1)
                i+=1
                break
            elif (line[i].isdigit()):
                a+=line[i]
                i+=1
            else:
                return (0, i,-1,-1)

        while (i<len(line)):
            if (line[i] == ')'):
                if (len(b)==0):
                    return (0, i+1, -1,-1)
                i+=1
                break
            elif (line[i].isdigit()):
                b+=line[i]
                i+=1
            else:
                return (0, i,-1,-1)
        return (1, i, int(a), int(b))

    else:
        return (0, 1,-1,-1)

    pass

def solve(data):
    sol=0
    i=0
    while(i<len(data)):
        valid, offset,a,b = pos_after_mul(data[i:])
        if (valid):
            sol += (a*b)
            i+=offset
        else:
            i+=offset
    return sol

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data = fp.read()
        sol = solve(data)
    print("Solution:", sol)

if __name__ == '__main__':
    main(*sys.argv[1:])