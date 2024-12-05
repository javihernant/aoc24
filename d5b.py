import sys

def build_rdic(rules):
    d = {}
    for r in rules:
        if (r[0] not in d):
            d[r[0]] = set([r[1]])
        else:
            d[r[0]].add(r[1])
    return d

def valid_update(update, rdic):
    n = len(update)
    i=1
    while (i<n):
        el=update[i]
        j=i-1
        while(j>=0):
            if(el in rdic and update[j] in rdic[el]):
                return False
            j-=1
        i+=1
    return True
    
def sort(update, rdic):
    n = len(update)
    i=1
    while (i<n):
        el=update[i]
        j=i-1
        replace=-1
        k=-1
        while(j>=0):
            if(el in rdic and update[j] in rdic[el]):
                k=j
            j-=1
        if (k>=0):
            update.pop(i)
            update.insert(k,el)
        i+=1
    return True

def solve(rules, updates):
    rdic = build_rdic(rules)
    sol=0
    for u in updates:
        if (not valid_update(u, rdic)):
            sort(u,rdic)
            sol+=u[int(len(u)/2)]
    return sol

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data = fp.read()
        rules, updates = data.split('\n\n')
        rules=[[int(el) for el in r.split('|')] for r in rules.splitlines()]
        updates=[[int(num) for num in u.split(',')] for u in updates.splitlines()]
        sol = solve(rules, updates)
    print("Solution:", sol)

if __name__ == '__main__':
    main(*sys.argv[1:])
