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

#def solve(gmap, h, w):
#    sol=0
#    i,j = find_guard(gmap,h,w)
#    di,dj = -1,0
#    visited=set()
#    while (True):
#        #print(i,j)
#        if ((i,j) not in visited):
#            sol+=1
#        nxti=i+di
#        nxtj=j+dj
#        if (nxti<0 or nxti>=h or nxtj<0 or nxtj>=w):
#            break
#        while (gmap[nxti][nxtj] == '#'):
#            di, dj = turn(di,dj)
#            nxti=i+di
#            nxtj=j+dj
#
#        if (nxti<0 or nxti>=h or nxtj<0 or nxtj>=w):
#            break
#        visited.add((i,j))
#        i=nxti
#        j=nxtj
#    return sol

#returns true if cycle
def guard_walk(guard_pos, obs_pos, gmap, dims):
    h, w = dims
    i, j = guard_pos
    gmap_cpy = [[e for e in row] for row in gmap]
    gmap_cpy[obs_pos[0]][obs_pos[1]] = '#'
    di,dj = -1,0
    visited=set([(i,j,di,dj)])
    while True:
        inext=i+di
        jnext=j+dj
        if (inext<0 or inext>=h or jnext<0 or jnext>=w):
            return False
        cnt = 0
        while (gmap_cpy[inext][jnext] == '#'):
            if cnt == 4:
                return True
            di, dj = turn(di,dj)
            inext=i+di
            jnext=j+dj
            cnt+=1

        if (inext<0 or inext>=h or jnext<0 or jnext>=w):
            print("exit")
            return False
        i=inext
        j=jnext
        if ((i,j, di,dj) not in visited):
            visited.add((i,j, di,dj))
        else:
            return True
    return False


def solve(gmap, h, w):
    i,j = find_guard(gmap,h,w)
    sol = 0
    for obsi in range(h):
        for obsj in range(w):
            if guard_walk((i,j), (obsi,obsj), gmap, (h,w)):
                sol += 1
    #guard_walk((i,j),(7,6), gmap, (h,w))

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

def test():
    pass

if __name__ == '__main__':
    #test()
    main(*sys.argv[1:])
