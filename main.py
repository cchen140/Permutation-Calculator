import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def nPr(n,r):
    f = math.factorial
    return f(n) / f(n-r)

def totalPermutation(n):
    r = 0
    for x in range(n+1):
        r += nPr(n,x)
    return r

if __name__ == '__main__':
    for i in range(10):
        print(i, ": ", totalPermutation(i))
