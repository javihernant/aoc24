import sys

def isXmas(i,j,mx, m, n):
    return (((mx[i][j-1]=='M' and mx[i+1][j]=='A' and mx[i+2][j+1]=='S') or (mx[i][j-1]=='S' and mx[i+1][j]=='A' and mx[i+2][j+1]=='M'))
            and ((mx[i][j+1]=='M' and mx[i+1][j]=='A' and mx[i+2][j-1]=='S') or (mx[i][j+1]=='S' and mx[i+1][j]=='A' and mx[i+2][j-1]=='M')))

def solve(data):
    sol=0
    mx = data.splitlines()
    m = len(mx)
    n = len(mx[0])
    i=0
    while(i<m-2):
        j=1
        while (j<n-1):
            if (isXmas(i,j,mx,m,n)):
                #print(i,j)
                sol+=1
            j+=1
        i+=1
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
