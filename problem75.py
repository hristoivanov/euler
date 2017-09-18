import time
start=time.time()

def getABC(m, n):
    pow2m = m**2
    pow2n = n**2
    return pow2m-pow2n, 2*m*n, pow2m+pow2n


def coprime(a, b):
    while b != 0:
        a, b = b, a%b
    return a == 1


maxL = 1500000
Ls = [0] * (maxL+1)

n = 0
while True:
    n += 1
    m = n-1
    resultsFound = 0
    while True:
        m += 2
        
        if coprime(n, m) == False:
            continue

        a, b, c = getABC(m,n)

        L = a+b+c
        if L > maxL:
            break

        resultsFound += 1
        for aux in range(L, maxL, L):
            Ls[aux] += 1

    if resultsFound == 0:
        break


the_ans = len([ True for num in Ls if num==1])
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
