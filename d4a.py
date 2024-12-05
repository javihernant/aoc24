import sys

def xmasInCol(i,col,mx, m, n):
    if (i+3>=m):
        return False
    return ((mx[i][col]=='X' and mx[i+1][col]=='M' and mx[i+2][col]=='A' and mx[i+3][col]=='S')
        or (mx[i][col]=='S' and mx[i+1][col]=='A' and mx[i+2][col]=='M' and mx[i+3][col]=='X'))

def xmasInRDiag(i,j,mx, m, n):
    if (i+3>=m or j+3 >=n):
        return False
    return ((mx[i][j]=='X' and mx[i+1][j+1]=='M' and mx[i+2][j+2]=='A' and mx[i+3][j+3]=='S')
        or (mx[i][j]=='S' and mx[i+1][j+1]=='A' and mx[i+2][j+2]=='M' and mx[i+3][j+3]=='X'))

def xmasInLDiag(i,j,mx, m, n):
    if (i+3>=m or j-3<0):
        return False
    return ((mx[i][j]=='X' and mx[i+1][j-1]=='M' and mx[i+2][j-2]=='A' and mx[i+3][j-3]=='S')
        or (mx[i][j]=='S' and mx[i+1][j-1]=='A' and mx[i+2][j-2]=='M' and mx[i+3][j-3]=='X'))

def solve(data):
    sol=0
    mx = data.splitlines()
    m = len(mx)
    n = len(mx[0])
    i=0
    while(i<m):
        j=0
        while (j<n):
            if (j+3<n and (mx[i][j:j+4] == 'XMAS' or mx[i][j:j+4] == 'SAMX')):
                #print(i,j)
                sol+=1
            if (xmasInCol(i,j,mx, m, n)):
                #print(i,j)
                sol+=1
            if (xmasInLDiag(i,j,mx, m, n)):
                #print(i,j)
                sol+=1
            if (xmasInRDiag(i,j,mx, m, n)):
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
