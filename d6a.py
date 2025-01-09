import sys

def find_guard(gmap, h, w):
    for i in range(h):
        for j in range(w):
            el = gmap[i][j]
            if (el=='^'):
                return i,j
    print("error")
    return (-1,-1)

def turn(di, dj):
    if (di==1):
        return (0,-1)
    elif (di==-1):
        return (0,1)
    elif (dj==1):
        return (1,0)
    elif (dj==-1):
        return (-1,0)
    else:
        print("error")
        return (0,0)

def solve(gmap, h, w):
    sol=0
    i,j = find_guard(gmap,h,w)
    di,dj = -1,0
    visited=set()
    while (True):
        #print(i,j)
        if ((i,j) not in visited):
            sol+=1
        nxti=i+di
        nxtj=j+dj
        if (nxti<0 or nxti>=h or nxtj<0 or nxtj>=w):
            break
        while (gmap[nxti][nxtj] == '#'):
            di, dj = turn(di,dj)
            nxti=i+di
            nxtj=j+dj

        if (nxti<0 or nxti>=h or nxtj<0 or nxtj>=w):
            break
        visited.add((i,j))
        i=nxti
        j=nxtj
    return sol

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data = fp.read()
        gmap = data.splitlines()
        h=len(gmap)
        w=len(gmap[0])
        sol = solve(gmap,h,w)
    print("Solution:", sol)

if __name__ == '__main__':
    main(*sys.argv[1:])
