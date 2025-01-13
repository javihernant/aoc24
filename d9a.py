import sys

def checksum(used, new):
    i=0
    j=0
    idx=0
    sol=0
    while (i<len(used) and j<len(new)):
        if (used[i][0] < new[j][0]):
            c=used[i][2]      
            while (c>0):
                sol+= used[i][1]* idx
                c-=1
                idx+=1
            i+=1
        else:
            c=new[j][2]      
            while (c>0):
                sol+= new[j][1]* idx
                c-=1
                idx+=1
            j+=1

    if (i<len(used)):
        c=used[i][2]      
        while (c>0):
            sol+= used[i][1]* idx
            c-=1
            idx+=1
        i+=1

    if (j<len(new)):
        c=new[j][2]      
        while (c>0):
            sol+= new[j][1]* idx
            c-=1
            idx+=1
        j+=1

    return sol

def solve(data):
    free = [ (i, data[i]) for i in range(1, len(data), 2)]
    free.reverse()
    used = [ (i, idn, data[i]) for idn,i in enumerate(range(0, len(data), 2))]
    new = []
    while (len(free) > 0 and len(used)>0):
        if (used[-1][0] < free[-1][0]):
            break
        tmp_u = used.pop()
        tmp_f = free.pop()
        if (tmp_f[1] > tmp_u[2]):
            tmp_f = (tmp_f[0], tmp_f[1] - tmp_u[2])
            free.append(tmp_f)
            new.append((tmp_f[0], tmp_u[1], tmp_u[2]))
        else:
            dif = tmp_u[2]-tmp_f[1]
            if (dif > 0):
                used.append((tmp_u[0],tmp_u[1], dif))
            new.append((tmp_f[0], tmp_u[1], tmp_f[1]))
    return (checksum(used, new))

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data = fp.read()
        data = [int(c) for c in data[:-1]]
        sol = solve(data)
        print("Solution:", sol)

def test():
    pass
    

if __name__ == '__main__':
    #test()
    main(*sys.argv[1:])
